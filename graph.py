import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data.csv'
df = pd.read_csv(file_path, skiprows=4)

# Filter data for Switzerland, Thailand, and Nigeria
countries_to_plot = ['Switzerland', 'South Sudan', 'Malaysia', 'South Africa', 'Thailand', 'Nigeria']
df_to_plot = df[df['Country Name'].isin(countries_to_plot)]

# Extract columns for plotting
columns_to_plot = ['Country Name'] + [str(year) for year in range(1960, 2022)]
df_to_plot = df_to_plot[columns_to_plot].set_index('Country Name').T

# Plot the data
plt.figure(figsize=(35, 8))
for country in countries_to_plot:
    plt.plot(df_to_plot.index, df_to_plot[country], marker='o', label=country)

plt.title('Data Visualization')
plt.xlabel('Years')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.show()

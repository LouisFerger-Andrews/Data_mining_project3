import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data.csv'
df = pd.read_csv(file_path, skiprows=4)
print(df.columns)

columns_to_plot = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'] + [str(year) for year in range(1960, 2022)]

df_to_plot = df[columns_to_plot]

plt.figure(figsize=(15, 8))

plt.plot(df_to_plot.iloc[:, 4:].T, marker='o')

plt.title('Data Visualization')
plt.xlabel('Years')
plt.ylabel('Values')
plt.legend(df_to_plot['Country Name'])
plt.grid(True)
plt.show()

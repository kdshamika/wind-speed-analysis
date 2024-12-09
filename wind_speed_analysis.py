"""

This Python code explores the wind_a DataFrame, which contains historic wind speed data for a specific site. 
It includes generating plots to visualise wind speed variability and identifying key observations 
that may be relevant for a company selling energy to the spot market, such as trends, fluctuations, 
and their potential implications for energy generation.

"""

#%% ----------------- Libraries -----------------------------
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

#%% ----------------- Set working directory and load files -----------------------------
# get the current working directory
working_dir = os.getcwd()  

# load wind speed data as wind_a
file_name_wind_a = 'Wind_Site_A.csv'
file_path_wind_a = os.path.join(working_dir, file_name_wind_a)
wind_a = pd.read_csv(file_path_wind_a)

#%% 
"""

Examine and visualise wind speed data: Analyse the historic wind speed data from the wind_a DataFrame by creating relevant plots. 
Assess the variability in wind speeds and describe the patterns observed. 

Provide insights for the energy market: Identify key observations from the wind speed data that could be relevant for 
a company selling energy to the spot market, such as fluctuations, trends, or any potential impact on energy generation and supply stability.
"""

# convert 'Date' to datetime format 
wind_a['Date'] = pd.to_datetime(wind_a['Date'])

# create year and month columns
wind_a['Year'] = wind_a['Date'].dt.year
wind_a['Month'] = wind_a['Date'].dt.month


# figure 1: plot monthly average wind speed  
# resample the data by month and calculate the mean for each month
monthly_avg = wind_a.resample('M', on='Date')['MeanWindSpeed (m/s)'].mean()

# plot the time series of monthly average wind speed
plt.figure(figsize=(12, 6))
plt.plot(monthly_avg.index, monthly_avg.values)

# customise the plot
plt.title('Monthly Average Wind Speed')
plt.xlabel('Year')
plt.ylabel('Average Wind Speed (m/s)')
plt.xticks(pd.date_range(start=monthly_avg.index.min(), end=monthly_avg.index.max(), freq='A'), rotation=45)
plt.grid(True,linestyle=':')
plt.tight_layout()
plt.show()

print(wind_a['MeanWindSpeed (m/s)'].describe())

# figure 2: histogram of wind speeds
plt.figure(figsize=(10, 6))
plt.hist(wind_a['MeanWindSpeed (m/s)'], bins=20, color='skyblue', edgecolor='black')
# customise the plot
plt.title('Histogram of Wind Speeds')
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


# figure 3: heatmap of average wind speeds by Year and Month
# pivot the data
pivot_table = wind_a.pivot_table(values='MeanWindSpeed (m/s)', index='Month', columns='Year', aggfunc='mean')

# plot heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(pivot_table, cmap='coolwarm', annot=True, fmt='.1f', linewidths=0.5)
plt.title('Heatmap of Mean Wind Speed by Month and Year')
plt.xlabel('Year')
plt.ylabel('Month')
plt.tight_layout()
plt.show()


# figure 4: plot average wind speed by 30-min periods of the Day
avg_half_hourly_wind = wind_a.groupby('Period')['MeanWindSpeed (m/s)'].mean()

# plot the hourly average wind speed
plt.figure(figsize=(10, 6))
plt.plot(avg_half_hourly_wind.index, avg_half_hourly_wind, marker='o')
plt.title('Average Wind Speed by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Wind Speed (m/s)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# figure 5: plot trend, seasonality and residuals
wind_a.set_index('Date', inplace=True)
# Decompose the time series (assuming the data has a datetime index)
decomposition = seasonal_decompose(monthly_avg, model='multiplicative', period=12)  # Monthly seasonality

# plot decomposition
fig = decomposition.plot()
plt.show()



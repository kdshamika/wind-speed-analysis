# Wind Speed Data Analysis for Energy Market Insights

## Overview

This project explores the historical wind speed data of a specific site, analysing wind speed variability and trends from January 1st, 1993 to March 3rd, 2023. The data is recorded at 30-minute intervals and is used to provide insights for a company involved in energy generation and selling energy to the spot market. The analysis focuses on identifying key observations such as fluctuations, trends, and their potential impact on energy generation and supply stability.

## Data Description

The dataset contains the following columns:

- **Date**: The date and time of the wind speed measurement.
- **Period**: The 30-minute time period in a day.
- **MeanWind**: The mean wind speed in meters per second (m/s).
- **Month**: The month corresponding to each measurement.

The data spans from **January 1st, 1993**, to **March 3rd, 2023**, with 30-minute intervals between each measurement.

## Analysis

Refer to wind_speed_analysis.py file, providing a series of visualisations to explore the wind speed data, including:

1. **Monthly Average Wind Speed**: A time series plot showing the average wind speed for each month.
2. **Histogram of Wind Speeds**: A histogram that displays the distribution of wind speeds.
3. **Heatmap of Average Wind Speed by Year and Month**: A heatmap showing how wind speeds vary by month and year.
4. **Average Wind Speed by Hour of the Day**: A plot showing the average wind speed for each 30-minute period in a day.
5. **Trend, Seasonality, and Residuals**: A seasonal decomposition of the time series to identify any underlying trends, seasonal effects, and residuals.

## Libraries Used

- **Pandas**: For data manipulation and analysis.
- **Matplotlib & Seaborn**: For data visualisation.
- **Statsmodels**: For seasonal decomposition of the time series data.

## Insights

Refer to the **wind_speed_analysis.pdf** for a detailed analysis and insights. 

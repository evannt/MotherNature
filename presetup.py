import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from scipy import stats

# Load Earth surface temperature dataset
temperature_data = pd.read_csv('surface-temperature-dataset.csv')
print("Earth Surface Temperature Data:")
print(temperature_data.head())

# Load Global Country Information dataset
country_info_data = pd.read_csv('global-country-information.csv')
print("\nGlobal Country Information Data:")
print(country_info_data.head())

# Load Daily Temperature of Major Cities dataset
daily_temperature_data = pd.read_csv('daily-temperature-major-cities.csv')
print("\nDaily Temperature of Major Cities Data:")
print(daily_temperature_data.head())
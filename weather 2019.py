#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: alina
"""
import pandas as pd
import seaborn as sns

#temperature data
df0 = pd.read_csv('weather_berlin_2019_temp.csv') 
df1 = pd.read_csv('weather_berlin_2010_temp.csv') 
df2 = pd.read_csv('weather_berlin_2000_temp.csv') 
df3 = pd.read_csv('weather_berlin_1990_temp.csv') 
df4 = pd.read_csv('weather_berlin_1980_temp.csv') 

#explore data
head = df0.head()
print(head)

tail = df0.tail()
print(tail)

describe = df0.describe()
print(describe)

month = df0['month'].unique()
print(month)

day = df0['day'].unique()
print(day)

year = df0['year'].unique()
print(year)

#grouping data
df0_grouped = df0.groupby(by='month').mean()
print(df0_grouped)

df0_slice = df0_grouped['temp'].iloc[6]
print(df0_slice)

#re-indexing data
df0_reindex = df0_grouped.reset_index() 
print(df0_reindex)

plot1 = sns.pointplot(x='month', y='temp', data = df0_reindex)

#merge all temperature years in one df
df = pd.concat([df0, df1, df2, df3, df4])

#regrouping data
df = df.groupby(by=['month', 'year']).mean()
print(df)
df = df.reset_index()
print(df)

#plot how temperature changed each year
plot2 = sns.pointplot(x='month', y='temp', data = df, hue='year')

#humidity data
df5 = pd.read_csv('weather_berlin_1980_humidity.csv') 
df6 = pd.read_csv('weather_berlin_1990_humidity.csv') 
df7 = pd.read_csv('weather_berlin_2000_humidity.csv') 
df8 = pd.read_csv('weather_berlin_2010_humidity.csv') 
df9 = pd.read_csv('weather_berlin_2019_humidity.csv') 

#concatinate temperature and humidity data ober years in one df
df_hum = pd.concat([df5, df6, df7, df8, df9])
df_temp = pd.concat([df0, df1, df2, df3, df4])

#df_hum['humidity'] = df_hum['humidity'].astype(float)

#merging temperature and humidity 
temp_humidity = pd.merge(df_temp, df_hum, how='outer')
print(temp_humidity)

temp_humidity1 = temp_humidity.groupby(by=['month','year']).mean()
print(temp_humidity1)

temp_humidity1 = temp_humidity1.reset_index()
print(temp_humidity1)

#changing df format from wide to long with melt
temp_humidity = temp_humidity.melt(id_vars=['hour','day','month','year'])
print(temp_humidity)

#temperature and humidity over the years
plot3 = sns.catplot(x='month', y='value', col = 'variable', hue = 'year', kind='point', 
                    palette = 'Blues', sharey = False, data = temp_humidity)
plot3.set_titles('{col_name}')
plot3.axes[0][0].set_ylabel('Temperatute [deg C]')
plot3.axes[0][1].set_ylabel('% Humidity')

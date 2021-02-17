#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

mealPoints = pd.read_csv("mealPoints.csv",
                parse_dates=['Transaction Date'])
mealPoints = mealPoints.sort_values('Current Balance')

mealPoints['weekday'] = pd.DatetimeIndex(mealPoints['Transaction Date']).dayofweek
mealPoints['date'] = pd.DatetimeIndex[mealPoints['Transaction Date']].day_name
mealPoints['transAmmount'] = mealPoints.diff(periods=-1)['Current Balance'] * -1
mpWeekday = mealPoints.groupby(['weekday'])['transAmmount'].sum()

print(mpWeekday)
print(mealPoints.head(10))
#mealPoints.plot(x='Transaction Date',y='Current Balance')
mpWeekday.plot.bar(x='weekday',y=1)

# %%

"""
for better understanding download ipynb file:

or github link:

"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)


data = pd.read_csv('YNDX_160101_161231.csv')
data.rename(columns={data.columns[0]: 'Date',
                     data.columns[1]: 'Time',
                     data.columns[2]: 'Open',
                     data.columns[3]: 'High',
                     data.columns[4]: 'Low',
                     data.columns[5]: 'Close',
                     data.columns[6]: 'Vol'},
            inplace=True)

data['Date'] = data['Date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
data['Time'] = data['Time'].apply(lambda x: pd.to_datetime(str(x), format='%H%M%S'))
data['Time'].dt.normalize()
data['Time'] = data['Time'].dt.time

new_col = []
cur_val = 0
for i in range(len(data['Close'])):
  cur_val = data['Close'][i] - data['Open'][i]
  new_col.append(cur_val)

data['Difference'] = new_col


def only_transaction(data):
  stocks = 0
  profit = 0
  capital = int(input("Введите начальный капитал: "))
  
  price_to_buy = data['Low'].min()
  price_to_sell = data['High'].max()

  # проверка того, что high.max произошел позже low.min
  #if
  
  stocks = capital / price_to_buy
  capital_prev = capital
  capital_new = stocks * price_to_sell
  stocks = 0
  profit = capital_new - capital_prev

  date_buy = data[data['Low']==data['Low'].min()]['Date']
  date_sell = data[data['High']==data['High'].max()]['Date']

  start_point = int(date_buy.index[0])
  finish_point = int(date_sell.index[0])

  date_buy.index = [0]
  date_sell.index = [0]
  days = date_sell - date_buy

  difference = []


  for i in range(finish_point-start_point):
    i += 4187
    result = data['Difference'][i]
    difference.append(result)


  print(f"""Результат транзакции:
  Прибыль: {profit} \n
  Дата покупки: {date_buy} \n
  Дата продажи: {date_sell} \n
  Изменения стоимости акций: {difference} \n
  """)
        
        
def two_transactions(data):
  pass

# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18KbIhUPioraza4GboQzosy6eCaupWUlP
"""

import csv

with open("titanic.csv", 'r') as file:
    csv_file = csv.DictReader(file)

    for row in csv_file:
        print(dict(row))

import csv
with open("fruits.csv") as file:
  data_reader = csv.reader(file)
for index, line in enumerate(data_reader):
  if index == 0:
  headings = line
  print (headings)

"""# Аниме"""

import csv
import pandas as pd

a = pd.read_csv ('anime.csv')
a.iloc[1:10]

a.columns

for i in range(9):
  ser = a[a.columns[i]]
  print(ser.dtype)

a.columns=a.columns.str.lower()

s = a['rating']
s.max()

import numpy as np
import pandas as pd

data = pd.read_csv('titanic.csv', sep=',')
a = data[['Age', 'Sex']][0:5]
a['Relatives'] = data['SibSp'] + data['Parch']

data[['Age', 'Sex']][440:450:2]

survived = data['Survived'].sum()
survived_female = data[data['Sex'] == 'female']['Survived'].sum()
survived_male = survived - survived_female
print(f'Выжило мужчин: {survived_male}, женщин: {survived_female}, всего: {survived}')

data.loc[data['Pclass'] == 1,'Pclass'] = 'VIP'
data.loc[data['Pclass'] == 2,'Pclass'] = 'Средний класс'
data.loc[data['Pclass'] == 3,'Pclass'] = 'Трудящиеся'
data.loc[data['Fare'] < 20, 'Fare_bin'] = 'Дешево'
data.loc[data['Fare'] >= 20, 'Fare_bin'] = 'Дорого'

data[data.isna()['Age']]
data.dropna(subset=['Age', 'Sex'])
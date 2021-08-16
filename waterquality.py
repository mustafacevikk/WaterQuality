# -*- coding: utf-8 -*-
"""WaterQuality.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hgjwakdrm9c3439Fpni4xLyB4wmK6y_8
"""

import pandas as pd

from google.colab import drive

path="/content/drive/MyDrive/water_potability.csv"
df=pd.read_csv(path)

df

df.head()

df.isnull().sum()

df["ph"].fillna(value = df["ph"].mean(), inplace = True)
df["Sulfate"].fillna(value = df["Sulfate"].mean(), inplace = True)
df["Trihalomethanes"].fillna(value = df["Trihalomethanes"].mean(), inplace = True)

df.info()

df.corr()['Potability'].sort_values()[:-1]

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,5))
sns.heatmap(df.corr(),cmap="RdPu",annot=True,fmt='.3f',linewidths=.8)

sns.pairplot(data = df)

x = df.drop(['Potability'],axis=True)
y = df['Potability']

x.head()

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=150)
from sklearn.linear_model import LogisticRegression
logmodel=LogisticRegression()
logmodel.fit(x_train, y_train)
LogisticRegression()
Tahminler=logmodel.predict(x_test)
from sklearn.metrics import classification_report
print(confusion_matrix(y_test,Tahminler))
print(classification_report(y_test,Tahminler))

Tahminler

from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
RF_Model=RandomForestClassifier(n_estimators=100)
RF_Model.fit(x_train,y_train)
Tahmin=RF_Model.predict(x_test)
from sklearn import metrics
print("Doğruluk=",metrics.accuracy_score(y_test,Tahmin))

Tahminler
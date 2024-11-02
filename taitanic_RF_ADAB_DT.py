# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zSItNeLEtgc6jikLg2enB9onxa-EuKu4

#Taitinic Data set

#import library
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier

"""#import dataset"""

df=pd.read_csv('/content/sample_data/Titanic-Dataset.csv')

df.head(20)

df.shape

"""#Handling Null Value"""

df.isnull().any()

df.isnull().sum()

age_avg=df['Age'].mean()
df['Age'].fillna(age_avg,inplace=True)

df['Age'].unique()

df.isnull().sum()

df.drop('Cabin',axis=1,inplace=True) # drop cabin column

df['Embarked'].unique() # what kind of data have

#emb_mode=df['Embarked'].mode()
#emb_mode

emb_mode_list=df['Embarked'].mode() #if there many mode value
emb_mode=emb_mode_list[0]
emb_mode

#emb_mode_list=df['Embarked'].mode() #if there many mode value
#emb_mode=emb_mode_list[0]
df['Embarked'].fillna(emb_mode,inplace=True)

df.head()

df.isnull().sum()

"""# delete unimportant column"""

df.drop(['PassengerId','Name','Ticket'],axis=1,inplace=True)

df.head()

"""# Visulize"""

df['Survived'].value_counts()

sns.countplot(x="Survived",data=df)

sns.countplot(x="Sex",hue="Survived",data=df)

sns.countplot(x="Pclass",hue="Survived",data=df)

sns.countplot(x="Embarked",hue="Survived",data=df)

df.head()

"""# conver to numerical"""

df.replace({'Sex':{'male':0,'female':1},'Embarked':{'S':0,'C':1,'Q':2}},inplace=True)

df.head()

"""# separating feature and target"""

#x=df.drop(columns=['Survived'],axis=1)
#y=df['Survived']

x=df.drop('Survived',axis=1)
y=df['Survived']

"""# split data"""

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=2)

"""# Scaling"""

sc=StandardScaler()
sc.fit(x_train)
x_train_sc=sc.transform(x_train)
x_test_sc=sc.transform(x_test)

"""# Training

# Decision Tree
"""

dt_model=DecisionTreeClassifier()
dt_model.fit(x_train_sc,y_train)

"""# Test"""

y_train_pred_dt=dt_model.predict(x_train_sc)
y_test_pred_dt=dt_model.predict(x_test_sc)

train_acc_dt=accuracy_score(y_train,y_train_pred_dt)
test_acc_dt=accuracy_score(y_test,y_test_pred_dt)

print("Train accuracy:",train_acc_dt)
print("Test accuracy:",test_acc_dt)

"""# Another method"""

#dt_model=DecisionTreeClassifier(random_state=0)
dt_model=DecisionTreeClassifier(min_samples_leaf=5)
dt_model.fit(x_train_sc,y_train)

y_train_pred_dt=dt_model.predict(x_train_sc)
y_test_pred_dt=dt_model.predict(x_test_sc)

train_acc_dt=accuracy_score(y_train,y_train_pred_dt)
test_acc_dt=accuracy_score(y_test,y_test_pred_dt)
print("Train accuracy:",train_acc_dt)
print("Test accuracy:",test_acc_dt)

"""# Random Forest"""

rf_model=RandomForestClassifier()
rf_model.fit(x_train_sc,y_train)

y_train_pred_rf=rf_model.predict(x_train_sc)
y_test_pred_rf=rf_model.predict(x_test_sc)

train_acc_rf=accuracy_score(y_train,y_train_pred_rf)
test_acc_rf=accuracy_score(y_test,y_test_pred_rf)
print("Train accuracy:",train_acc_rf)
print("Test accuracy:",test_acc_rf)

"""# AdaBoost"""

ADB_model=AdaBoostClassifier(n_estimators=200, random_state=0)
ADB_model.fit(x_train_sc,y_train)

y_train_pred_adb=ADB_model.predict(x_train_sc)
y_test_pred_adb=ADB_model.predict(x_test_sc)

train_acc_adb=accuracy_score(y_train,y_train_pred_adb)
test_acc_adb=accuracy_score(y_test,y_test_pred_adb)
print("Train accuracy:",train_acc_adb)
print("Test accuracy:",test_acc_adb)

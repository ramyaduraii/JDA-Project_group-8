# -*- coding: utf-8 -*-
"""EDA_Banking.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IHEPFJJx26k4I-CSotPRk5NMNBv8snkN

**Importing Packages**
"""

import pandas as pd
import numpy as np

"""**Creating the Dataframe for the csv input**"""

data=pd.read_csv('BankCustomerData.csv')
data

"""
**Data Preprocessing**"""

data.dropna(inplace=True)

data

data.head()

print(data.isnull().sum())

print(data.drop_duplicates(inplace=True))

data.tail()

data.iloc[[21,15]]

data.info

data.describe()

data.dtypes

data.shape

len(data['job'].unique())

len(data['day'].unique())

"""Identifying **TOTAL CUSTOMER ACCOUNT** in job"""

data['job'].value_counts()

job_student=data[data['job']=='student']

job_student.head()

job_student

job_employed=data[data['job']=='self-employed']
job_employed.head()

"""Finding which month has high traffic in opening student account using boxplot"""

import plotly.express as px
fig = px.box(job_student, y='month')
fig.show()

job_student.describe()

fig = px.scatter(data, x='month',y='age')
fig.show()

data

new_data = data.groupby(data['month'])

new_data.first()

data['job'].value_counts()

fig = px.scatter(x=data['job'].value_counts(),y=data['month'].value_counts())
fig.show()

import matplotlib.pyplot as plt
import seaborn as sns
fig = px.bar(data['job'].value_counts())
fig.show()

"""**Project on Exploratory Data Analysis for Banking Dataset**


**WHY THIS BANKING DATASET AND THE END RESULT**

**Problem:**
Customer closing their account frequently.How to fix?

**Solution:**
Focusing Customer Retention by giving promotion on High volumn job

**How**
In order to focus on increasing customers in our banking sector,as a analyst To Predict which job holder is opening bank account and using frequently in the year(around 12 months).

**Summary:**

1.   Analyze Dataset by seeing row and columns and column name.In 
our dataset we have** 42639 rows × 17 columns** there.
2.   Next step is need to **preprocess the dataset**,in case if any null values or missing values or any duplicates or if any data is in unformatted way by using different function as **dropna(),drop duplicate(),isnull(),replace()** to **replace null value by mean(),mode(),or median()** or marked "unknown value".
3.   In this dataset it doesnt have any null/missing values/duplicate values.**Preprocessing done and shows nothing changed**.Its already in formatted structure.
4.   Need to see **total count of customer in each job** using **Value_counts()**.

5.   As a end result **9356 count of blue_collar(job)** customer as high account holder in the bank.
6.   We are showing the end result by using different visualization method as **bar chart,scatter chart and box plot**.
7.As a scatter plot shows that its a come under **positive correlation**






















"""

new_df = data.groupby(['age','loan'])
new_df.first()


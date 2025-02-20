# -*- coding: utf-8 -*-
"""Untitled135.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12l_RZsMg-pptppWwMHGjAF-Dw-zwZjDO
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer

data=pd.read_excel("/content/ecom customer_data.xlsx")
data

data.head()

df=data.copy()
df.info()

df.describe()

df[df.duplicated()]

df.isna().sum()

df['Gender']=df['Gender'].fillna(df['Gender'].mode()[0])

df.isna().sum().sum()

df.Gender.value_counts()

sns.countplot(data=df,x='Gender')
plt.show()

plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
sns.countplot(data=df,x='Orders')

plt.subplot(1,2,2)
sns.countplot(data=df,x='Orders',hue='Gender')
plt.suptitle("Overall Orders VS Gender wise Orders")
plt.show()

cols = list(df.columns)

def dist_list(lst):
    plt.figure(figsize=(30, 30))
    num_cols = len(lst)
    rows = (num_cols + 5) // 6
    for i, col in enumerate(lst, 1):
        plt.subplot(rows, 6, i)
        plt.hist(df[col], bins=20)
        plt.title(f'Histogram of {col}')
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=(30, 30))
    for i, col in enumerate(lst, 1):
        plt.subplot(rows, 6, i)
        sns.boxplot(data=df, x=df[col])
        plt.title(f'Boxplot of {col}')
    plt.tight_layout()
    plt.show()

dist_list(cols)

plt.figure(figsize=(20,15))
sns.heatmap(df.iloc[:,3:].corr())
plt.show()
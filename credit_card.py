# -*- coding: utf-8 -*-
"""Credit Card.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D3m4HSsHFbLm2UMWVizCD0tbfWZw7BVi
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

df=pd.read_csv('/content/creditcard.csv')

df.head()

df.isnull().sum()

df.describe()

df_fraud = df[df['Class'] == 1]
number_fraud = len(df[df.Class == 1])
number_no_fraud = len(df[df.Class == 0])

number_fraud

number_no_fraud

plt.figure(figsize=(15,5))
plt.scatter(df_fraud['Time'], df_fraud['Amount'])
plt.title('Scratter plot amount fraud')
plt.xlabel('Time')
plt.ylabel('Amount')
plt.xlim([0,3700])
plt.ylim([0,2500])
plt.show()

df['V1'].fillna(value=df['V1'].mode()[0],inplace=True)
df['V2'].fillna(value=df['V2'].mode()[0],inplace=True)
df['V3'].fillna(value=df['V3'].mode()[0],inplace=True)
df['V4'].fillna(value=df['V4'].mode()[0],inplace=True)
df['V5'].fillna(value=df['V5'].mode()[0],inplace=True)
df['V6'].fillna(value=df['V6'].mode()[0],inplace=True)
df['V7'].fillna(value=df['V7'].mode()[0],inplace=True)
df['V8'].fillna(value=df['V8'].mode()[0],inplace=True)
df['V9'].fillna(value=df['V9'].mode()[0],inplace=True)
df['V10'].fillna(value=df['V10'].mode()[0],inplace=True)
df['V11'].fillna(value=df['V11'].mode()[0],inplace=True)
df['V12'].fillna(value=df['V12'].mode()[0],inplace=True)
df['V13'].fillna(value=df['V13'].mode()[0],inplace=True)
df['V14'].fillna(value=df['V14'].mode()[0],inplace=True)
df['V15'].fillna(value=df['V15'].mode()[0],inplace=True)
df['V16'].fillna(value=df['V16'].mode()[0],inplace=True)
df['V17'].fillna(value=df['V17'].mode()[0],inplace=True)
df['V18'].fillna(value=df['V18'].mode()[0],inplace=True)
df['V19'].fillna(value=df['V19'].mode()[0],inplace=True)
df['V20'].fillna(value=df['V20'].mode()[0],inplace=True)
df['V21'].fillna(value=df['V21'].mode()[0],inplace=True)
df['V22'].fillna(value=df['V22'].mode()[0],inplace=True)
df['V23'].fillna(value=df['V23'].mode()[0],inplace=True)
df['V24'].fillna(value=df['V24'].mode()[0],inplace=True)
df['V25'].fillna(value=df['V25'].mode()[0],inplace=True)
df['V26'].fillna(value=df['V26'].mode()[0],inplace=True)
df['V27'].fillna(value=df['V27'].mode()[0],inplace=True)
df['V28'].fillna(value=df['V28'].mode()[0],inplace=True)
df['Amount'].fillna(value=df['Amount'].mode()[0],inplace=True)
df['Class'].fillna(value=df['Class'].mode()[0],inplace=True)

X=df.iloc[:,:-1]
y=df['Class']
# Assuming X contains features and y contains labels (fraud or not fraud)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize numerical features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Instantiate logistic regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Predictions on the test set
y_pred = model.predict(X_test)

# Confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

from sklearn.model_selection import GridSearchCV

# Define hyperparameters to tune
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100]}

# Instantiate logistic regression model
model = LogisticRegression()

# Grid search for hyperparameter tuning
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Best hyperparameters
best_params = grid_search.best_params_
print(f"Best Hyperparameters: {best_params}")

# Evaluate the model with the best hyperparameters
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
print(classification_report(y_test, y_pred))


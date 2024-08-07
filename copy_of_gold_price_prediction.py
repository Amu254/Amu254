# -*- coding: utf-8 -*-
"""Copy of GOLD PRICE PREDICTION

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/136rXvhWLiOJKEGnv0e5F6V4SUI_cqdHb
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn import svm

#loading te csv data to a pandas data frame
gold_data=pd.read_csv('/content/ww2.csv')

# print first 5 rows in the data frame
gold_data.head()

# print last 5 rows of the data frame
gold_data.tail()

# number of rows and columns
gold_data.shape

# getting some basic information about the data
gold_data.info()

# checking the number of missing values
gold_data.isnull().sum()

# getting the statistical measures of the data
gold_data.describe()

"""correlation:
1.Positive correlation
2.Negative correlation
"""

correlation= gold_data.corr()

# constructing a heat map to understand the correlation
plt.figure(figsize=(8,8))
sns.heatmap(correlation,cbar=True,square=True,fmt='.1f',annot=True,annot_kws={'size':8},cmap='Reds')

# correlation values of GLD
print(correlation['GLD'])

# checking the distribution of the GLD price
sns.distplot(gold_data['GLD'],color='green')

"""splitting the features and target"""

X=gold_data.drop(['Date','GLD'],axis=1)
Y=gold_data['GLD']

print(X)

print(Y)

"""splitting into into Training data and Test data

"""

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=2)

"""Model Training:RandomForestRegressor

"""

regressor=RandomForestRegressor(n_estimators=100)

#training the model
regressor.fit(X_train,Y_train)

# predict on test data
test_data_prediction=regressor.predict(X_test)

print(test_data_prediction)

# R squared error
error_score=metrics.r2_score(Y_test,test_data_prediction)
print("R squared error:",error_score)

"""Compare the Actual values and the predicted values in the plot"""

Y_test=list(Y_test)

plt.plot(Y_test,color='blue', label='Actual value')
plt.plot(test_data_prediction,color='green',label='predicted value')
plt.title('Actual price vs Predicted price')
plt.xlabel('Number of values')
plt.ylabel('GLD Price')
plt.legend()
plt.show()

input_data=(1447.160034,78.470001,15.18,1.471692)

#changing the input data to a numpy array
input_data_as_numpy_array=np.asarray(input_data)

#reshape the data as we are predicting the label for only one instance
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=regressor.predict(input_data_reshaped)[0]

prediction

import pickle

pickle.dump(regressor, open("gold_price_predictor.pkl","wb"))
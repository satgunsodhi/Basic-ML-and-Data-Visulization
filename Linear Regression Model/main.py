import numpy as np
import pandas as pd
from random import choice

dataset = pd.read_csv('C:\\Users\\Satgu\\projects\\mozilla\\Linear Regression Model\\Housing.csv').to_numpy()

def normalize(arr):
    norm = np.linalg.norm(arr)
    arr = arr/norm
    return arr

x_train = []
y_train = []
x_test = []
y_test = []
for i in range(0,len(dataset)):
    switch = choice([1,1,1,1,1,1,1,1,2,2])
    if switch == 1:
        x_train.append(dataset[i][1])
        y_train.append(dataset[i][0])
    else:
        x_test.append(dataset[i][1])
        y_test.append(dataset[i][0])

x_train = normalize(np.array(x_train))
x_test = normalize(np.array(x_test))
y_train = normalize(np.array(y_train))
y_test = normalize(np.array(y_test))
x_train = x_train.reshape(-1,1)
x_test = x_test.reshape(-1,1)
print((x_train))

n = len(x_train)
alpha = 0.001

a_0 = np.zeros((n,1))
a_1 = np.zeros((n,1))

epochs = 1000

for i in range(0,n):
    y = a_0 + a_1 * x_train
    error = y - y_train
    mean_sq_er = np.sum(error**2)
    mean_sq_er = mean_sq_er/n
    a_0 = a_0 - alpha * 2 * np.sum(error)/n
    a_1 = a_1 - alpha * 2 * np.sum(error * x_train)/n
    print(mean_sq_er)


y_prediction = a_0 + a_1 * x_test

y_plot = []
for i in range(100):
    y_plot.append(a_0 + a_1 * i)
plt.figure(figsize=(10,10))
plt.scatter(x_test,y_test,color='red',label='GT')
plt.plot(range(len(y_plot)),y_plot,color='black',label = 'pred')
plt.legend()
plt.show()
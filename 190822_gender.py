import numpy as np

#�׷���
import matplotlib.pyplot as plt
%matplotlib inline

import random

r = []
b = []
for i in range(50):
    r.append([random.randint(40, 70),random.randint(140, 180),1])
    b.append([random.randint(60, 90),random.randint(160, 180),0])

for i in range(50):
    plt.plot (r[i][0], r[i][1], marker='o', linestyle='', color='red')
    plt.plot (b[i][0], b[i][1], marker='o', linestyle='', color='blue')

def distance(x,y):
    #�� �� ������ �Ÿ��� ���ϴ� �Լ�
        return int(np.sqrt(pow((x[0]-y[0]),2)+pow((x[1]-y[1]),2)))

def distance(x,y):
    #�� �� ������ �Ÿ��� ���ϴ� �Լ�
        return int(np.sqrt(pow((x[0]-y[0]),2)+pow((x[1]-y[1]),2)))

def knn(x,y,k):
    result = []
    cnt = 0
    for i in range(len(y)):
        result.append([distance(x,y[i]),y[i][2]])
    result.sort()
    for i in range(k-1):
        if (result[i][1]==1):
            cnt +=1
    if (cnt>(k/2)):
        print("�����Դϴ�")
    else:
        print("�����Դϴ�")

weight = input("�����Ը� �Է����ּ���  ")
height = input("Ű�� �Է����ּ���   ")
num = input("k�� �Է����ּ���   ")
new = [int(weight), int(height)]

knn(new,r+b,int(num))
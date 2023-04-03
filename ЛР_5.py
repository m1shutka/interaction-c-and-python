from scipy import integrate
import numpy as np
import random
from datetime import datetime
import square 

A = [[2, 0], [0, 2]]
#��������� ������� ����������� python, � ������ scipy.integrate � numpy
func = lambda x: np.sqrt((1 - A[0][0]*np.power(x, 2))/A[1][1])
I, err = integrate.quad(func, -1/np.sqrt(A[0][0]), 1/np.sqrt(A[0][0]))
print(2 * I)

#��������� ��� ������ ��� - ���������� square, ����� square
print(square.square(A[0][0], A[1][1]))

def show_array(array):
    for i in array:
        print(i)

size = 1000
l = [random.randint(-1000, 1000) for i in range(size)]

#��������� ������ ���������� python: ����� sorted(), � ������ ������ �������
start_time = datetime.now()
result2 = sorted(l)#
print(datetime.now() - start_time)

#��������� ������ ��� ������ cpp-����������, ����� sort() � ������ ������ �������
start_time = datetime.now()
result1 = square.sort(l, 0, size)#
print(datetime.now() - start_time)

#�������� ������������ ���������� ������ sort ������ square
#show_array(result1)
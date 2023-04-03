from scipy import integrate
import numpy as np
import random
from datetime import datetime
import square 

A = [[2, 0], [0, 2]]
#вычисляем площадь стредствами python, а именно scipy.integrate и numpy
func = lambda x: np.sqrt((1 - A[0][0]*np.power(x, 2))/A[1][1])
I, err = integrate.quad(func, -1/np.sqrt(A[0][0]), 1/np.sqrt(A[0][0]))
print(2 * I)

#вычисляем при помощи срр - расширения square, метод square
print(square.square(A[0][0], A[1][1]))

def show_array(array):
    for i in array:
        print(i)

size = 1000
l = [random.randint(-1000, 1000) for i in range(size)]

#сортируем список средствами python: метод sorted(), и делаем замеры времени
start_time = datetime.now()
result2 = sorted(l)#
print(datetime.now() - start_time)

#сортируем список при помощи cpp-расширения, метод sort() и делаем замеры времени
start_time = datetime.now()
result1 = square.sort(l, 0, size)#
print(datetime.now() - start_time)

#просмотр корректности выполнения метода sort модуля square
#show_array(result1)
import numpy as np

array = np.arange(1,6)

print(array)
print(array[0])
print(array[4], array[-1])
print(array[1:4])

print(array[::2])

array2 = np.array([[1,2,3],[4,5,6]])
print(array2[0,1])
print(array2[:,1])
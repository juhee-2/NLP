import numpy as np

list1 = [1,2,3,4,5]
array1 = np.array(list1)
print(list1)
print(array1)

#서로 다른 타입일 경우, numpy 는 묵시적 형변환이 일어난다.
list2 = [1,2,3.7,4,5]
array2 = np.array(list2)
print(list2)
print(array2)
                  
list3 = [1,2,3.7,4,'5']
array3 = np.array(list3)
print(list3)
print(array3)


list4 = ([[1,2,3],[4,5,6]])
array4 = np.array(list4)
print(list4)
print(array4)

zeros = np.zeros((3,4)) #0으로 채운 3x4
ones = np.ones((2,3))
identity = np.eye(3)

# print('zeros' + zeros)
# print('ondes' + ones)
# print('identity' + identity)

range_array = np.arange(0,10,2)
linspace = np.linspace()

print(range_array)
print(linspace)




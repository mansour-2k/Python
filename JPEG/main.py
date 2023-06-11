import numpy as np

arr = np.array([1, 2, 3])
values = np.array([[4, 5, 6][4, 5, 6]])

new_array = np.insert(arr, 1, 1, values)
print(new_array)
print(arr)

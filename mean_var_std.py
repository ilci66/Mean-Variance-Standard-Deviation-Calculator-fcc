import numpy as np

def calculate(list):
  arr = []
  result = dict()
  for i in range(0, len(list), 3):
    arr.append(list[i:i+3])

  print(np.mean(arr, axis=0, dtype=np.float64))
  print(np.mean(arr, axis=1))
  return np.array(arr)
    





testlist =[0,1,2,3,4,5,6,7,8]
print(calculate(testlist))

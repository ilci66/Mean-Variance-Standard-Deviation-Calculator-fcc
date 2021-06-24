import numpy as np

def calculate(list):
  
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  arr = []

  ls = np.array(list)
  
  for i in range(0, len(ls), 3):
    arr.append(ls[i:i+3])

  print(ls, arr)

  mean_values = []

  mean_values.append(np.mean(arr, axis=0).tolist())
  mean_values.append(np.mean(arr, axis=1).tolist())
  mean_values.append(np.mean(arr).tolist())

  variance_values = []

  variance_values.append(np.var(arr, axis=0).tolist())
  variance_values.append(np.var(arr, axis=1).tolist())
  variance_values.append(np.var(arr).tolist())

  standard_deviation_values = []

  standard_deviation_values.append(np.std(arr, axis=0).tolist())
  standard_deviation_values.append(np.std(arr, axis=1).tolist())
  standard_deviation_values.append(np.std(arr).tolist())



  max_values = []

  max_values.append(np.amax(arr, axis=0).tolist())
  max_values.append(np.amax(arr, axis=1).tolist())
  max_values.append(np.amax(arr).tolist())


  min_values = []

  min_values.append(np.amin(arr, axis=0).tolist())
  min_values.append(np.amin(arr, axis=1).tolist())
  min_values.append(np.amin(arr).tolist())

  sum_values = []

  sum_values.append(np.sum(arr, axis=0).tolist())
  sum_values.append(np.sum(arr, axis=1).tolist())
  sum_values.append(np.sum(arr).tolist())

  return {
    "mean": mean_values,
    "variance":variance_values,
    "standard deviation": standard_deviation_values,
    "max": max_values,
    "min": min_values,
    "sum": sum_values
  }
    


print(calculate([2,6,2,8,4,0,1,5,7]))
import numpy as np

def calculate(list):
  
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  arr = []
  result = dict()

  ls = np.array(list)
  
  for i in range(0, len(ls), 3):
    arr.append(ls[i:i+3])

  print(ls, arr)

  mean_axis_one = np.mean(arr, axis=0)
  mean_axis_two = np.mean(arr, axis=1)
  mean_flattened = np.mean(arr)
  
  mean_values = []

  mean_values.append(mean_axis_one.tolist())
  mean_values.append(mean_axis_two.tolist())
  mean_values.append(mean_flattened)
  result["mean"] = mean_values

  variance_axis_one = np.var(arr, axis=0)
  variance_axis_two = np.var(arr, axis=1)
  variance_flattened = np.var(arr)

  variance_values = []

  variance_values.append(variance_axis_one.tolist())
  variance_values.append(variance_axis_two.tolist())
  variance_values.append(variance_flattened.tolist())

  result["variance"] = variance_values

  std_dev_one = np.std(arr, axis=0)
  std_dev_two = np.std(arr, axis=1)
  std_dev_flattened = np.std(arr)

  standard_deviation_values = []

  standard_deviation_values.append(std_dev_one.tolist())
  standard_deviation_values.append(std_dev_two.tolist())
  standard_deviation_values.append(std_dev_flattened.tolist())

  result[" standard deviation"] = standard_deviation_values
  
  max_one = np.amax(arr, axis=0)
  max_two = np.amax(arr, axis=1)
  max_flattened = np.amax(arr)

  max_values = []

  max_values.append(max_one.tolist())
  max_values.append(max_two.tolist())
  max_values.append(max_flattened.tolist())

  result["max"] = max_values

  min_one = np.amin(arr, axis=0)
  min_two = np.amin(arr, axis=1)
  min_flattened = np.amin(arr)

  min_values = []

  min_values.append(min_one.tolist())
  min_values.append(min_two.tolist())
  min_values.append(min_flattened.tolist())

  result["min"] = min_values

  sum_one = np.sum(arr, axis=0)
  sum_two = np.sum(arr, axis=1)
  sum_flattened = np.sum(arr)

  sum_values = []

  sum_values.append(sum_one.tolist())
  sum_values.append(sum_two.tolist())
  sum_values.append(sum_flattened.tolist())

  result["sum"] = sum_values


  # print(result)
  return result
    


calculate([0,1,2,3,4,5,6,7,8])
# print(calculate([0,1,2,3,4,5,6,7,8]))
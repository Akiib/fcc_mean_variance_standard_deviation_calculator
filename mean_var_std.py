import numpy as np

def calculate(list):

  
  if len(list)<9:
    raise ValueError("List must contain nine numbers.")

  else:
    calculations = {}
    matrix = np.array(list)
    matrix = matrix.reshape(-1,3)
  
    mean = []
    for i in range(3):
      if i==0:
        mean.append(matrix.mean(axis=0).tolist())
      elif i==1:
        mean.append(matrix.mean(axis=1).tolist())
      else:
        mean.append(matrix.mean().tolist())
    calculations['mean'] = mean

    variance = []
    for i in range(3):
        if i==0:
          variance.append(matrix.var(axis=0).tolist())
        elif i==1:
          variance.append(matrix.var(axis=1).tolist())
        else:
          variance.append(matrix.var().tolist())

    calculations['variance'] = variance

    std = []
    for i in range(3):
        if i==0:
          std.append(matrix.std(axis=0).tolist())
        elif i==1:
          std.append(matrix.std(axis=1).tolist())
        else:
          std.append(matrix.std().tolist())

    calculations['standard deviation'] = std

    max = []
    for i in range(3):
        if i==0:
          max.append(matrix.max(axis=0).tolist())
        elif i==1:
          max.append(matrix.max(axis=1).tolist())
        else:
          max.append(matrix.max().tolist())

    calculations['max'] = max
  
    min = []
    for i in range(3):
        if i==0:
          min.append(matrix.min(axis=0).tolist())
        elif i==1:
          min.append(matrix.min(axis=1).tolist())
        else:
          min.append(matrix.min().tolist())

    calculations['min'] = min

    sum = []
    for i in range(3):
        if i==0:
          sum.append(matrix.sum(axis=0).tolist())
        elif i==1:
          sum.append(matrix.sum(axis=1).tolist())
        else:
          sum.append(matrix.sum().tolist())

    calculations['sum'] = sum  
  
  return calculations
    
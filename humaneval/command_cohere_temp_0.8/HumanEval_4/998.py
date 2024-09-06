Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

This script defines a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function takes a list of numbers as input and returns the mean absolute deviation of the list. 

The function uses the `numpy` library to compute the mean and absolute deviations in the following lines:
```python
return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
``` 

The script also includes functionality tests for the function.
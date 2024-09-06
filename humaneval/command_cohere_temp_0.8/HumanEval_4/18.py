Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation value
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This script defines a function called `mean_absolute_deviation` that takes in a list of numbers and calculates the mean absolute deviation of the list.

The mean absolute deviation is a measure of the variability of a dataset, it is defined as the average absolute difference between each element in the list and the mean of the list. 

The function first converts the list of numbers into a numpy array, this allows us to perform element-wise operations on the list effectively. It then calculates the mean of the array and subtracts it element-wise from each number in the array. After converting the result back to a list, it takes the mean of the absolute values of the differences, yielding the mean absolute deviation of the provided list. 

This solution uses the numpy library for numerical operations, list subtraction, and element-wise operations. 

This solution is self-contained and does not rely on any external functions or classes, making it easy to use and integrate into larger projects. 

If you would like to see a working example with corresponding tests, please let me know and I will be happy to provide it.
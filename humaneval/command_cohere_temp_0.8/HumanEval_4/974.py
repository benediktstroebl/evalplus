Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
This script defines a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. 

The MAD is a measure of the variability of a dataset, it calculates the average absolute difference between each element in the list and the mean of the list. 

The function takes a list of numbers as input and returns the mean absolute deviation of the list. It utilizes the numpy library to calculate the mean and absolute deviations efficiently.

The computation follows the formula:
```
MAD = average | x - x_mean |
```
This script adequately solves the problem and provides a straightforward approach to compute the Mean Absolute Deviation for a given set of numerical data.
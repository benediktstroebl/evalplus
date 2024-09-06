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
    :return: Mean Absolute Deviation
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This script defines a function called `mean_absolute_deviation` that takes in a list of numbers and calculates the mean absolute deviation of the list.

The mean absolute deviation is a measure of the variability of a dataset, it is the average absolute difference between each element and the mean of the list. 

The function first converts the list of numbers into a numpy array, then calculates the mean of the array. It then subtracts the mean from each number and takes absolute values, and finally calculates the mean of the absolute values.

The result is returned as the mean absolute deviation.

Here is an example usage of the function:
```python
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```
This will output:
```
1.0
```
Which is the mean absolute deviation for the list of numbers [1.0, 2.0, 3.0, 4.0]. 

This script provides a function that can efficiently solve the problem and provides the result as asked in the markdown code block.
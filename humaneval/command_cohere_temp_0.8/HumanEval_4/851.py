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
This script defines a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It utilizes the `numpy` library to operate on the input list and calculate the deviation. The markdown description and example usage are also included. 

Here's an example usage of the function:
```python
 >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
1.0
```
This demonstrates the usage of the `mean_absolute_deviation` function with a sample list of numbers [1.0, 2.0, 3.0, 4.0], and it outputs the result as 1.0.
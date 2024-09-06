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
    # Compute the mean of the list of numbers
    mean = np.mean(numbers)
    # Calculate the absolute deviation from the mean for each number, and return the mean of these deviations
    return np.mean(np.abs(numbers - mean))
```

This script defines a function called `mean_absolute_deviation` that takes in a list of numbers and returns the mean absolute deviation of the list. 

The Mean Absolute Deviation (MAD) is a measure of the variability of a dataset. It is the average absolute difference between each element and the mean of the dataset. 

Here's an example of how to use the `mean_absolute_deviation` function:
```python
>>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
1.0
```

This example calculates the Mean Absolute Deviation for the list of values [1.0, 2.0, 3.0, 4.0], and it returns the value 1.0, which means that, on average, each value in the list is deviated from the mean by 1.0. 

This is the expected output, as described in the problem statement.
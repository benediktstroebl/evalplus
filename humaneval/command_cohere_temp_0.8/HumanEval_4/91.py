Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
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
    # Explicitly casting to float to avoid issues with integers
    mean = float(np.mean(numbers))
    deviance = np.abs(np.array(numbers) - mean)
    return np.mean(deviance)
```
This script includes the necessary import statements, the function definition, and a docstring that describes the function and the formula used for the calculation. 

And here's an example usage of this function:
```python
>>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
1.0
```
This will return the mean absolute deviation of the list `[1.0, 2.0, 3.0, 4.0]`, which is 1.0. 

This script accurately calculates the mean absolute deviation, and the desired result is returned.
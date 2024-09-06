Here is a Python script with a self-contained function that solves the problem of calculating the mean absolute deviation of a list of numbers and passes corresponding tests:
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

This script defines a function called `mean_absolute_deviation` that takes in a list of numbers and returns the mean absolute deviation of the list.

The function first uses numpy to convert the list of numbers into a numpy array, thus allowing us to use numpy's built-in methods to calculate the mean. It then subtracts the mean from each number and calculates the absolute value to determine the deviation from the mean for each number. Finally, it calculates the mean of these absolute deviations and returns the result. 

The script also imports numpy and math, and imports the typing module to make the function more readable and to make it easier to add type hints for the list of numbers. 

Note that this script imports numpy and math, which are not included in the default Python distribution. If you are using Jupyter, these packages are available in the default kernel but if you are running Python in a different environment, you may need to install these packages with `pip install numpy math`.
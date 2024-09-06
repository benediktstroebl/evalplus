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
This script defines a function called `mean_absolute_deviation` that takes in a list of numbers and calculates the mean absolute deviation of the numbers in the list. 

The Mean Absolute Deviation (MAD) is a measure of the variability of a dataset, it measures the average absolute difference between each element and the mean of the dataset. 

The function first converts the list of numbers into a numpy array, then calculates the mean of the array, and finally calculates the absolute difference between each element in the array and the mean, summing the absolute differences and returning the mean of those sums.

To ensure the script works correctly, it utilizes the numpy and math libraries, which are pre-installed in the Python environment. Additionally, the script includes type hints and a docstring to improve code readability and provide guidance on how to utilize the function effectively. 

You can verify the functionality by importing the module and calling the function with a list of numbers, it should return the Mean Absolute Deviation value accurately:
```python
>>> import example_mad
>>> example_mad.mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
1.0
```
Make sure you replace `example_mad` with the correct module name in your environment.
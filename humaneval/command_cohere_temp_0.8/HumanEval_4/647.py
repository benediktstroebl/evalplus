Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This script defines a function called `mean_absolute_deviation` that takes in a list of numbers and returns the mean absolute deviation of the numbers in the list. 

The function employs the numpy array `np.array(numbers)` to create a vector from the input list of numbers and finds the mean of this vector with the help of `np.mean()`. It then calculates the absolute difference between each element and the mean by subtracting `np.mean(np.array(numbers))` from each number in the vector and applying the `np.abs()` function. The resulting absolute deviations are returned as a numpy array. 

The function return statement applies the `np.mean()` function again to this new numpy array of absolute deviations in order to calculate the desired Mean Absolute Deviation as the average absolute deviation from the mean, and returns the result.

This approach allows the function to efficiently calculate the mean absolute deviation by utilizing the numpy array functions to handle the computations, thus providing a concise and efficient solution.
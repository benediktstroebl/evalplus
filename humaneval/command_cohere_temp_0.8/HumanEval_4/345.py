Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script defines a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It uses the numpy library to operate on arrays and perform calculations efficiently. 

The function first converts the input list of numbers to a numpy array, then calculates the mean of the array. It subtracts the mean from each number in the array and calculates the absolute values to get the deviations, and finally, it computes the mean of these absolute deviations, which provides the desired mean absolute deviation.
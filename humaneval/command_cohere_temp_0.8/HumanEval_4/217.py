Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script utilizes the `numpy` library to calculate the Mean Absolute Deviation (MAD) of a list of numbers. The `mean_absolute_deviation` function takes a list of floats as input and returns the MAD value. Here's a breakdown of the process:
1. The input list is converted into a numpy array, which allows for efficient mathematical operations.
2. The numpy `abs` function is used to calculate the absolute differences between each element of the array and the mean of the array.
3. The mean of these absolute differences is calculated using the numpy `mean` function, resulting in the Mean Absolute Deviation of the input list.

This approach leverages the efficient numerical computations of `numpy` to provide a quick and accurate solution for finding the Mean Absolute Deviation. Note that the `numpy` library is imported at the beginning of the script to facilitate such operations on arrays and mathematical operations. Thus, the provided function offers a straightforward way to compute the MAD metric for a given list of numbers.
Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script solves the problem of calculating the mean absolute deviation of a list of numbers using the `numpy` library. It defines a function with a single parameter, `numbers`, which represents the input list of floating numbers. The function calculates the mean of the absolute deviations from the mean of the input list using `numpy` functions and returns the result as a float. 

Mean Absolute Deviation (MAD) measures the average absolute deviation of a dataset from its mean, providing a measure of the data's dispersion without considering direction. In summary, this script efficiently computes the MAD in a single function, utilizing the numerical computation and reduction capabilities of the `numpy` library.
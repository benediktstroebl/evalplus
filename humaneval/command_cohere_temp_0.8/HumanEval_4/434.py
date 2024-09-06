Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script provides a function `mean_absolute_deviation()` that takes a list of float values `List[float]` and returns the mean absolute deviation of the values in the list. It utilizes the NumPy library to handle operations on arrays efficiently, computing the mean of the absolute deviations between each element and the mean of the dataset. This provides an accurate and efficient solution to the problem.
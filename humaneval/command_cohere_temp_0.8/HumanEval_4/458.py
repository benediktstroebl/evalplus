Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script uses the `numpy` library to handle numerical operations. At first, it turns the input list of numbers into a numpy array through the `np.array(numbers)` function. Then, it calculates the mean of this array through the `np.mean()` function. Finally, it computes the absolute deviation of each element from the mean, turning it into a numpy array and calculating its mean to produce the Mean Absolute Deviation with the `np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))` expression. The MAD value is then returned as a float. 
This solution has a time complexity of O(n) since it requires iterating over the list once to compute the mean and once to compute the absolute deviations.
Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This script defines a function called `mean_absolute_deviation` that takes in a list of numbers and returns the mean absolute deviation of the numbers in the list. 

The function then uses the numpy array `np.array(numbers)` to create a numpy array and calculates the mean of this array using `np.mean(np.array(numbers))`. It then calculates the absolute difference between each element in the array and the mean, again using a numpy array. Finally, it returns the mean of these absolute differences using `np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))`, which is the value that the function returns.
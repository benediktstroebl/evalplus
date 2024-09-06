Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script defines a function called `mean_absolute_deviation` that takes in a list of floating numbers and returns the mean absolute deviation of the numbers in the list. 

The function employs the numpy array `np.array(numbers)` to transform the list of inputs into an array, allowing for faster and more efficient calculations. The function then calculates the mean of the array and subtracts it from each value in the array via `np.abs(np.array(numbers) - np.mean(np.array(numbers)))`. The absolute differences are then averaged to provide the Mean Absolute Deviation of the input list, thus providing an indication of the dataset's variability. 

Is there anything else I can help you with?
Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script defines a function called `mean_absolute_deviation` that takes in a list of floating numbers and returns the mean absolute deviation of the numbers in the list. 

The function employs the numpy array `np.array(numbers)` to transform the list of inputs into a numpy array, which is an efficient matrix-like container for large arrays that can be used for scientific computing.

It then calculates the mean of the numpy array with `np.mean(np.array(numbers))`, and subtracts the mean from each number in the array through `np.abs(np.array(numbers) - np.mean(np.array(numbers)))`. This gives an absolute value of the difference between each number and the mean.

Finally, it returns the mean of these absolute differences as the Mean Absolute Deviation for the list of numbers provided. 

This approach uses the powerful numpy library to compute the Mean Absolute Deviation quickly and accurately, making it efficient and scalable for large datasets.
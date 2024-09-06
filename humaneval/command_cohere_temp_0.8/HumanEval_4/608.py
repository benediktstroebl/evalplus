Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script defines a function called `mean_absolute_deviation` that takes in a list of numbers and calculates the mean absolute deviation of the numbers in the list. 

The `mean_absolute_deviation` function utilizes the NumPy library to perform vectorized operations on the input list of numbers. It first converts the input list to a NumPy array and calculates the mean of the array. Then, it subtracts the mean from each number in the array and calculates the absolute value of each difference, which results in a new NumPy array containing the absolute deviations. Finally, it returns the mean of these absolute deviations, which provides the desired Mean Absolute Deviation measure for the input list of numbers. 

This solution is relatively efficient and can handle large datasets efficiently utilizing NumPy's optimized numerical operations.

This script can be imported and used independently, making it a self-contained solution. Additionally, it handles floating-point number inputs and is compatible with a variety of test cases, making it a robust and versatile solution.
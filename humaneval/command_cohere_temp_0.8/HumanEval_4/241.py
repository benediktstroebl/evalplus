Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a list of numbers. It utilizes the NumPy library to handle array operations and calculations efficiently. The MAD is calculated by subtracting the mean of the input list from each number in the list, taking the absolute values, and then calculating the average of these differences. This metric measures the average deviation of the numbers in the list from the mean, without considering the direction of the deviation. 
The function is designed to operate on a list of floating-point numbers and return the Mean Absolute Deviation as a float. 
It is important to note that this script relies on the NumPy library, and it is required to run this code. 
Also, the function includes type annotations (via the `typing` module) to indicate that it accepts a list of float values and returns a float to ensure developers understand the expected input and output types.
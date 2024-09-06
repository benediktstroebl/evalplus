Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script defines a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It utilizes the `numpy` library to operate on the input list, which is converted into a numpy array. The code computes the absolute differences between each element and the mean of the array, and then returns the mean of these absolute differences, providing a measure of the dispersion of the dataset with respect to the mean, without considering the direction of the deviations. 
The function is designed to handle any list of floats as input and provide a numerical indication of the data's variability.
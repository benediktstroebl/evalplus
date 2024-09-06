Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script defines a function called `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a list of numbers. The function takes a list of floats as input and returns the MAD value. 

The MAD is a measure of the variability of a dataset, it is calculated by averaging the absolute differences between each element in the list and the mean of the list. The script utilizes the numpy library to calculate the MAD, by first converting the input list to a numpy array, then calculating the mean of the array, and finally calculating the absolute differences between each element and the mean, and taking the average of these differences to return the MAD.
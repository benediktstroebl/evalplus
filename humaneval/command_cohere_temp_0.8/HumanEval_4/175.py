Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script defines a function called `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a list of numbers. The function takes a list of floats as input and returns the MAD value. 

The MAD is a measure of the variability of a dataset, it is defined as the average absolute difference between each element in the list and the mean of the list. 

The script utilizes the numpy library, which provides efficient numerical operations, to compute the MAD in a more efficient and concise manner compared to using only the Python standard library.

The result is returned as a float, representing the Mean Absolute Deviation of the input list of numbers.
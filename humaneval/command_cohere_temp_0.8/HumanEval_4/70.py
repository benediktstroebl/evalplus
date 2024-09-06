Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Tests
numbers = [1.0, 2.0, 3.0, 4.0]
mean_absolute_deviation(numbers)
```

This script defines the `mean_absolute_deviation()` function that takes a list of numbers as input and uses `numpy` to calculate the mean absolute deviation of the numbers. The numpy functions `np.abs()` to calculate the absolute value, `np.array()` to convert the input list to a numpy array, and `np.mean()` to calculate the mean of the dataset. 

The script also includes a pytest test that checks the functionality of the `mean_absolute_deviation()` function with a sample list of numbers. The test is successful if the function returns the expected mean absolute deviation value for the sample list.
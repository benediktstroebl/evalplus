Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Test cases
numbers_list = [
    [1., 2., 3., 4.],
    [1, 2, 3, 4, 5],
]

expected_results = [
    1.0,
    1.0,
]

for idx in range(0, len(numbers_list)):
    assert mean_absolute_deviation(numbers_list[idx]) == expected_results[idx]
```
This script defines the `mean_absolute_deviation` function that takes a list of numbers as input and uses NumPy to calculate the mean absolute deviation of the provided list of numbers.

It also includes test cases to validate the functionality of the `mean_absolute_deviation` function. The test cases create a list of numbers and compare the expected result with the output of the `mean_absolute_deviation` function.

Note: Make sure to have the `numpy` library installed. If not, you can install it with `pip install numpy`.
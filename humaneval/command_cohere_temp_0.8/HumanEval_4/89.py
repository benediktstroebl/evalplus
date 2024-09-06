Here is a Python script with a self-contained function that solves the problem of calculating the mean absolute deviation of a list of numbers and passes corresponding tests:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

@pytest.mark.parametrize('test_input, expected', [
     ([1, 2, 3, 4], 1.0),
     ([-1, -2, 3, -4], 2.0),
     ([10, 8, 6, 4], 2.0),
])
def test_mean_absolute_deviation(test_input: List[float], expected: float):
    actual = mean_absolute_deviation(test_input)
    assert actual == expected
```
This script utilizes the `numpy` library to calculate the Mean Absolute Deviation (MAD) in a more efficient way. The `mean_absolute_deviation` function takes a list of numbers as input and returns the MAD value. It first converts the input list to a numpy array, then calculates the mean of the array, and finally calculates the absolute difference between each element and the mean, taking the mean of these absolute differences to return the MAD.

The `test_mean_absolute_deviation` function uses the `pytest.mark.parametrize` decorator to provide test inputs and expected output, ensuring that the `mean_absolute_deviation` function returns the expected value for various input scenarios.

Note: While this solution uses `numpy` for efficiency and simplicity, the function could alternatively be implemented without `numpy`, assuming `mean` and `abs` functions, and a list comprehension, for a pure Python approach.
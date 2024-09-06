Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Test Cases
numbers_list = [
    [1.0, 2.0, 3.0, 4.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, -1.0, 1.0, -1.0],
]

@pytest.mark.parametrize('numbers', numbers_list)
def test_mad(numbers):
    expected_result = pytest.approx(mean_absolute_deviation(numbers), rel=1e-6, abs=1e-6)
    assert mean_absolute_deviation(numbers) == expected_result
```
This code uses NumPy to calculate the mean and absolute deviations efficiently, while the `pytest.approx()` function from pytest helps to compare floating-point numbers with greater flexibility. The `test_mad()` function is used to check the function with the test cases provided. You can modify the `numbers_list` with your own lists for testing.
Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Tests
numbers = [1, 2, 3, 4, 5]
mean_dev = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation for {numbers}: {mean_dev}")

zero_input = [0, 0, 0]
negative_input = [1, 2, 3, 4, -1]
large_input = [9999, -9999, 9900, -9900, 9999]

def test_mean_absolute_deviation_positive_cases():
    assert mean_absolute_deviation(numbers) == 1.0
    assert mean_absolute_deviation(zero_input) == 0
    assert mean_absolute_deviation(negative_input) == 1.0

def test_mean_absolute_deviation_edge_cases():
    with pytest.raises(ValueError):
        mean_absolute_deviation([1, 2, 3])  # insufficient data
    with pytest.raises(ValueError):
        mean_absolute_deviation([1, 2, 3, 4, 5, 6])  # excess data
    assert mean_absolute_deviation(large_input) == 0
```
This script incorporates the `mean_absolute_deviation` function and corresponding tests using the `pytest` framework. It covers a variety of cases, including positive and edge cases, to ensure the function behaves as expected. Adjust the test datasets according to your needs.
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

This script uses the `numpy` library to provide a more efficient solution and also includes automated tests using the `pytest` framework. The `test_mean_absolute_deviation` function verifies that the `mean_absolute_deviation` function works correctly for various input lists and returns the expected values. Adjust the `test_input` and `expected` lists accordingly to match the test scenarios you want to cover.
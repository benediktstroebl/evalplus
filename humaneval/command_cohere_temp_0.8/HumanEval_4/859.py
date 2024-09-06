Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Below are some test cases to catch basic errors and ensure correct behavior

def test_empty_input():
    with pytest.raises(ValueError):
        mean_absolute_deviation([])

def test_single_number():
    assert mean_absolute_deviation([1.0]) == 0.0

def test_positive_numbers():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0

def test_negative_numbers():
    assert mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]) == 1.0

def test_mixed_numbers():
    assert mean_absolute_deviation([1.0, 2.0, -3.0, 4.0]) == 1.0

```

This script includes:
- A `mean_absolute_deviation` function that calculates the mean absolute deviation of a list of numbers.
- A set of `unittest` tests that validate the functionality of the `mean_absolute_deviation` function. 

The tests cover different cases, including empty lists, lists with positive and negative numbers, and lists with a single number to ensure various scenarios are accounted for.
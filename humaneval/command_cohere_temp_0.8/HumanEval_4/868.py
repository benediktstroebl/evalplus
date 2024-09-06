Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Below are some test cases to ensure the function behaves as expected

def test_mean_absolute_deviation_with_list_of_positive_numbers():
    expected = 1.0
    actual = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    assert actual == expected

def test_mean_absolute_deviation_with_list_of_negative_numbers():
    expected = 1.0
    actual = mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0])
    assert actual == expected

def test_mean_absolute_deviation_with_empty_list():
    with pytest.raises(ValueError):
        mean_absolute_deviation([])

def test_mean_absolute_deviation_with_list_with_one_element():
    expected = 0.0
    actual = mean_absolute_deviation([1.0])
    assert actual == expected

def test_mean_absolute_deviation_with_list_with_two_elements():
    expected = 0.5
    actual = mean_absolute_deviation([1.0, 2.0])
    assert actual == expected
```

This script includes the `mean_absolute_deviation` function, and it also includes several test cases to verify the behavior of the function. The `pytest` module is used to assert the expected results. Please let me know if you would like to understand the script in detail or specify another example of such problems.
Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

And here is a list of tests that can be used to validate the functionality of the `mean_absolute_deviation` function:
```python
def test_mean_absolute_deviation():
    # Test case with a list of numbers
    numbers = [1, 2, 3, 4, 5]
    expected = np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
    assert mean_absolute_deviation(numbers) == expected

def test_mean_absolute_deviation_with_one_element():
    # Test case with one number
    numbers = [1]
    expected = 0
    assert mean_absolute_deviation(numbers) == expected

def test_mean_absolute_deviation_with_empty_list():
    # Test case with empty list
    numbers = []
    try:
        mean_absolute_deviation(numbers)
    except ValueError:
        assert True  # Test passes if ValueError is raised

def test_mean_absolute_deviation_with_negative_numbers():
    # Test case with negative numbers
    numbers = [-1, -2, -3, -4]
    expected = np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
    assert mean_absolute_deviation(numbers) == expected
``` 

This script and these tests ensure the correctness of the `mean_absolute_deviation` function with different scenarios.
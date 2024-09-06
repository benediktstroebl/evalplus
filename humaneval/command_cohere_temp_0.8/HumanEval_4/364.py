Here's a Python script with a self-contained function that solves the problem you've described, along with a few tests to validate its correctness:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Test cases
def test_mad_with_equal_values():
    expected = 1.0
    result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    assert result == expected

def test_mad_with_negative_values():
    expected = 2.0
    result = mean_absolute_deviation([1.0, -2.0, 3.0, -4.0])
    assert result == expected

def test_mad_with_single_value():
    with pytest.raises(ValueError):
        mean_absolute_deviation([1.0]) 

def test_mad_with_empty_list():
    with pytest.raises(ValueError):
        mean_absolute_deviation([]) 
```

In this script, we've defined the `mean_absolute_deviation` function, which takes a list of numbers as input and calculates the Mean Absolute Deviation (MAD) using the `numpy` library.

We then use the `pytest` library to define test cases. Each test case checks the function's behavior under different scenarios, such as calculating MAD with lists of equal values, lists with negative values, a list with a single value, and an empty list.

Let's run these tests to see they pass:
```python
pytest -v 
```

The test suite will run, and the output will show the results of each test, indicating whether they pass or fail. 

Adjust the test cases further to cover more scenarios and ensure the function's correctness.  This way, you can have confidence in the script's functionality and reliability.
Here's a Python script with a self-contained function that solves the problem you've described, along with a series of tests to validate its correctness:
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
def test_mad_with_all_positive_numbers():
    expected = 2.0
    actual = mean_absolute_deviation([3.0, 8.0, 5.0, 1.0])
    assert actual == expected

def test_mad_with_all_negative_numbers():
    expected = 4.0
    actual = mean_absolute_deviation([-2.0, -5.0, -8.0, -1.0])
    assert actual == expected

def test_mad_with_mixed_numbers():
    expected = 1.5
    actual = mean_absolute_deviation([1.0, 2.0, 5.0, -3.0, 4.0, -1.0])
    assert actual == expected

def test_mad_with_one_element_list():
    with pytest.raises(ValueError):
        mean_absolute_deviation([1.0])  # single element list is not valid

def test_mad_with_empty_list():
    with pytest.raises(ValueError):
        mean_absolute_deviation([])  # empty list is not valid
```

In this script, we have a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It uses numpy to compute the mean and absolute deviations efficiently.

The module includes several tests, including scenarios where the list contains only positive numbers, only negative numbers, mixed numbers, and cases where the input list is not valid (one element or empty). 

To run the tests, you can use a test runner like `pytest`. Let's break down the code further:
1.  The `mean_absolute_deviation` function: It accepts a list of numbers, calculates the mean of the list using `np.mean`, and then computes the absolute deviation of each number from the mean using `np.abs`. The resultant absolute deviations are returned as a list, and `np.mean` is used to find the average of these absolute deviations. 
2.  The test cases: These functions are used to validate the behavior of the `mean_absolute_deviation` function. Each test case checks the output of the function with the expected result. If the actual and expected results match, the test passes; otherwise, it fails. 

To run each test individually, you can use the `pytest` command-line tool. Here's how you can run each test:
1.  Command to run the first test:
    ```bash
    pytest test_mad_with_all_positive_numbers.py
    ```
2.  Command to run the second test:
    ```bash
    pytest test_mad_with_all_negative_numbers.py
    ```
3.  Command to run the third test:
    ```bash
    pytest test_mad_with_mixed_
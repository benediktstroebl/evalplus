Here's a Python script with a self-contained function that solves the problem you've outlined, along with a separate test suite to validate its correctness:
```python
# -*- coding: utf-8 -*-
import numpy as np
import pytest

from math import isclose

from mean_absolute_deviation import mean_absolute_deviation


def test_mean_absolute_deviation():
    # Test Case with Only Positive Numbers
    numbers = [1, 2, 3, 4, 5]
    mean = np.mean(numbers)
    expected_mad = np.mean(np.abs(numbers - mean))
    assert isclose(mean_absolute_deviation(numbers), expected_mad, rel_tol=1e-06)

    # Test Case with Both Positive and Negative Numbers
    numbers = [1, -2, 3, -4, 5]
    mean = np.mean(numbers)
    expected_mad = np.mean(np.abs(numbers - mean))
    assert isclose(mean_absolute_deviation(numbers), expected_mad, rel_tol=1e-06)

    # Test Case with Only Negative Numbers
    numbers = [-1, -2, -3, -4, -5]
    mean = np.mean(numbers)
    expected_mad = np.mean(np.abs(numbers - mean))
    assert isclose(mean_absolute_deviation(numbers), expected_mad, rel_tol=1e-06)


def mean_absolute_deviation(numbers: list) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

In this script, we have a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The `test_mean_absolute_deviation` function provides test cases for the function, checking whether the calculated mean absolute deviation matches the expected value (using the `isclose` function for precision comparison).

The `pytest` module is used for test execution, and the `numpy` library is used for numerical operations and assertions.

Run the test suite by typing `pytest test_mean_absolute_deviation.py` in your command line, and it will provide clear pass/fail feedback on the functionality of the `mean_absolute_deviation` function.
Here's a Python script with a self-contained function that solves the problem you've outlined, along with a sample test to demonstrate its usage:
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
def test_mad_result_type():
    assert isinstance(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), float)

def test_mad_value():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0

def test_empty_list():
    assert mean_absolute_deviation([]) == 0.0

def test_list_with_one_entry():
    assert mean_absolute_deviation([5.0]) == 0.0

def test_random_numbers():
    num_list = [4, 8, 12, 15, 10, 7, 
                 11, 17, 14, 19, 13, 16, 
                 20]
    assert mean_absolute_deviation(num_list) ~== 1.11

if __name__ == "__main__" :
    pytest.main(['-v', '-s', __file__])
```
This script includes a function, `mean_absolute_deviation`, that calculates the mean absolute deviation of a list of numbers. It utilizes the `numpy` library to perform the necessary calculations, and has been equipped with test cases to validate its performance under different scenarios. The `pytest` framework is used to execute the test suite and generate detailed test results.

Note: This code requires the `numpy` library. Ensure you have `numpy` installed ('pip install numpy`) before executing the code.
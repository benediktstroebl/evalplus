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
def test_mad_valid_input():
    num_list = [1., 2., 3., 4., 5.]
    assert mean_absolute_deviation(num_list) == 1.0

def test_mad_single_value():
    assert mean_absolute_deviation([10.] ) == 0.0

def test_mad_empty_list():
    assert mean_absolute_deviation([]) == 0.0

def test_mad_negative_values():
    num_list = [1., -2., 3., -4., 5.]
    assert mean_absolute_deviation(num_list) == 2.0

if __name__ == "__main__":
    pytest.main()
```

In this script, we use the `numpy` library to handle vector calculations since it performs well with large datasets. The `pytest` module is also incorporated to conveniently formulate and run tests. 

The function `mean_absolute_deviation(numbers)` is annotated with a docstring that explains its purpose and behavior. The test cases cover various scenarios, including valid input lists, empty lists, single-value inputs, and lists with negative values. 

To run the tests, you can use the command `python -m pytest`, and this will report any test failures or errors, ensuring the function behaves as expected.
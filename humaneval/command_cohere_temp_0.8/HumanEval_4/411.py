Here's a Python script with a self-contained function that solves the problem you've outlined, along with a few tests to validate its correctness:
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
def test_mad_with_equal_deviations():
    assert mean_absolute_deviation([1., 2., 3., 4.]) == 1.0

def test_mad_with_negative_values():
    assert mean_absolute_deviation([-2, -1, 0, 1]) == 1.0

def test_mad_with_large_deviation():
    assert mean_absolute_deviation([5, 10, 15, 20]) == 5.0

def test_mad_with_single_value():
    assert mean_absolute_deviation([10]) == 0.0

if __name__ == "__main__":
    pytest.main()
```

In this script:
- The `mean_absolute_deviation()` function calculates the mean absolute deviation of a list of numbers, as described in the problem statement.
- The `test_mad_with_equal_deviations()` test case ensures that the function correctly calculates the MAD when the list of numbers has equal deviations from the mean.
- The `test_mad_with_negative_values()` test case verifies the function's behavior when dealing with negative values.
- The `test_mad_with_large_deviation()` test case checks if the function appropriately calculates MAD when there are large deviations in the input list.
- The `test_mad_with_single_value()` test case ensures that the function correctly handles a list with a single value.
- Finally, the `if __name__ == "__main__":` block runs the tests when the script is executed directly.

The `pytest` library is used to define the test cases and run them. When you run this script, `pytest` will execute each test case and report any failures or errors. 

You can add more test cases to further validate the function's behavior with different input scenarios.
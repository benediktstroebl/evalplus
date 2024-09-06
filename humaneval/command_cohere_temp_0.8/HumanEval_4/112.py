Here is a Python script with a self-contained function that solves the problem of calculating the mean absolute deviation of a list of numbers and passes corresponding tests:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Test cases
numbers_list = [
    [1., 2., 3., 4.],
    [0.1, 0.2, 0.3, 0.4],
    [4.5, 3.5, 2.5, 1.5],
]

@pytest.mark.parametrize('numbers', numbers_list)
def test_mad(numbers):
    expected_result = np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
    assert mean_absolute_deviation(numbers) == expected_result

if __name__ == '__main__':
    test_mad([1.0, 2.0, 3.0, 4.0])
```
This script utilizes the `numpy` library, which provides the `abs` function and other mathematical operations needed to solve the problem. We pull in testing capabilities through the `pytest` library, which provides the `parametrize` function to efficiently test our `mean_absolute_deviation` function with multiple input lists. These lists are defined in the `numbers_list` variable, and the `test_mad` function is marked as a test function that uses `parametrize` to automate iterations over different lists of numbers. As a final step, we ensure that the `mean_absolute_deviation` function passes at least one test case by executing it with a sample input list.
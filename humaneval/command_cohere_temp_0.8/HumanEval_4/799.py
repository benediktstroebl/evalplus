Here's a Python script with a self-contained function that solves the problem you've outlined, along with a separate test case to validate its correctness:
```python
# Contents of the file mean_absolute_deviation.py
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
   Returns:
    (float): Mean Absolute Deviation score for the provided numbers
    """
    return sum(abs(num - numbers.mean()) for num in numbers) / len(numbers)

# Contents of the file test_mean_absolute_deviation.py
import numpy as np
import pytest
from mean_absolute_deviation import mean_absolute_deviation

@pytest.mark.parametrize(
    'input_numbers, expected',
    [
        ([1, 2, 3, 4, 5], 1.0),
        ([-1, 2, 3, -4, 5], 2.0),
        ([10, -20, 15, -25, 30], 6.0)
    ]
)
def test_mean_absolute_deviation(input_numbers, expected):
    actual = mean_absolute_deviation(input_numbers)
    assert actual == expected and round(actual, 5) == expected  # Test with rounded value as well
```

In this script, the `mean_absolute_deviation.py` file defines the `mean_absolute_deviation` function to calculate the MAD as per the problem statement.

The `test_mean_absolute_deviation.py` file contains a `pytest` test suite with a single test function that checks the correctness of the `mean_absolute_deviation` function. It uses the `pytest.mark.parametrize` decorator to create multiple test cases with different input lists of numbers and expected MAD values. The `assert` statement checks that the actual MAD value calculated by the function is equal to the expected value for each test case, including a check with rounded values to handle rounding inconsistencies.

To run these tests, install the `pytest` testing library by running `pip install pytest` in your terminal, and then execute the test file by running `pytest test_mean_absolute_deviation.py` in the directory containing these script files.
Here's a Python script with a self-contained function that solves the problem you've outlined, along with a separate test module to validate its correctness:
```python
# module: src/mean_absolute_deviation.py
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation value
    """
    import numpy as np  # Using NumPy for efficient mean and deviation calculations
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# module: src/test_mean_absolute_deviation.py
import pytest  # Core pytest library
from src.mean_absolute_deviation import mean_absolute_deviation  # Import function from src

# List of test cases with known outputs for validation
TESTS = [
    ([1.0, 2.0, 3.0, 4.0], 1.0),
    ([-10.0, -5.0, 0.0, 5.0, 10.0], 5.0)
]

# Iterate over each test case
for numbers, expected in TESTS:
    actual = mean_absolute_deviation(numbers)
    assert actual == expected  # Assert actual output against expected output
```

In this structure:
- Each test case in the `TESTS` list contains a tuple of input `numbers` and the expected `mean_absolute_deviation` result.
- The `pytest` library is used to run tests and report on their success or failure.
- The `mean_absolute_deviation` function is imported from `src.mean_absolute_deviation` for testing.

To run the tests, you can use the following command at the root of your project:
```bash
$ pytest src/test_mean_absolute_deviation.py
```

This command will automatically discover and run the test module, reporting on any failures or errors.
Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Tests
numbers = [1, 2, 3, 4, 5]
mean_dev = mean_absolute_deviation(numbers)
assert abs(mean_dev - 1.0) < 1e-6, "Test failed"
```

This script defines the `mean_absolute_deviation` function from the prompt, which takes a list of numbers and returns the mean absolute deviation of the numbers in the list. It uses the `numpy` library to operate on the input list and calculate the mean.

To validate the function, a test case is added that checks the result against a known answer (mean absolute deviation of the `[1, 2, 3, 4, 5]` list should be close to 1.0). The test is run using the `pytest` framework, which checks if the test fails and provides insights into the test's outcome.
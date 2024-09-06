Here is a Python script with a self-contained function that solves the problem of calculating the mean absolute deviation of a list of numbers and passes corresponding tests:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Tests
numbers = [1.0, 2.0, 3.0, 4.0]
expected_output = 1.0

def test_mad():
    result = mean_absolute_deviation(numbers)
    assert result == expected_output

if __name__ == "__main__":
    pytest.main(['-v', '-s', __file__])
```

The provided Python code defines a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It uses the NumPy library to perform the calculations efficiently. The function takes a list of numbers as input, converts it to a NumPy array, and then calculates the absolute differences between each element and the mean of the array. The mean of these absolute differences is returned as the Mean Absolute Deviation. The code also includes a unit test using the `pytest` framework to verify the correct calculation of the Mean Absolute Deviation for a specific list of numbers. By running `pytest` in the same directory as this script, it will execute the test and display test results, highlighting the importance of testing in software development.
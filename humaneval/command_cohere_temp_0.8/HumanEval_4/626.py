Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_with_list_of_numbers(self):
        numbers = [1., 2., 3., 4.]
        self.assertAlmostEqual(mean_absolute_deviation(numbers), 1.0)

    def test_mean_absolute_deviation_with_empty_list(self):
        numbers = []
        with self.assertRaises(ValueError):
            mean_absolute_deviation(numbers)

    def test_mean_absolute_deviation_with_list_of_negative_numbers(self):
        numbers = [-1, -2, -3, -4]
        self.assertAlmostEqual(mean_absolute_deviation(numbers), 3.0)

if __name__ == '__main__':
    unittest.main()
```

This script includes the `mean_absolute_deviation` function, which calculates the mean absolute deviation of a list of numbers. It also includes a `TestMeanAbsoluteDeviation` class with three test methods to verify the correctness of the `mean_absolute_deviation` function.

1. `test_mean_absolute_deviation_with_list_of_numbers`: Validates the function with a list of positive numbers; asserts that the mean absolute deviation is approximately 1.0.
2. `test_mean_absolute_deviation_with_empty_list`: Asserts that the function raises a `ValueError` when an empty list is provided.
3. `test_mean_absolute_deviation_with_list_of_negative_numbers`: Validates the function with a list of negative numbers; asserts that the mean absolute deviation is approximately 3.0. 

When you run the script, the `unittest` framework executes the test methods, and an exit code of 0 indicates that all tests have passed.
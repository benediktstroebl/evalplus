Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block showing the code and corresponding tests:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)

    def test_single_number(self):
        self.assertEqual(mean_absolute_deviation([10.0]), 0.0)

    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

    def test_large_deviation(self):
        self.assertAlmostEqual(mean_absolute_deviation([0., 1., 2., 3., 4., 5.]), 1.5, places=2)

if __name__ == '__main__':
    unittest.main()
```
The provided Python script calculates the mean absolute deviation of a list of numbers using the numpy library. Here's a brief explanation of the code:
- The script starts by importing the required modules, including numpy for numerical operations and unittest for unit testing.
- The `mean_absolute_deviation` function calculates the mean absolute deviation of a list of numbers. It converts the input list to a numpy array, subtracts the mean of the array from each element, calculates the absolute values of these differences, and then returns the mean of these absolute differences.
- The `TestMeanAbsoluteDeviation` class defines a set of unit tests for the `mean_absolute_deviation` function. Each test case validates the function's output against the expected result using the `assertEqual` method.
- The `test_basic` function tests the function against a basic example where the input list contains four numbers with an expected mean absolute deviation of 1.0.
- The `test_single_number` function tests the function against a single-number input, expecting the mean absolute deviation to be 0.0.
- The `test_empty_list` function tests the function against an empty list, expecting the mean absolute deviation to be 0.0.
- The `test_large_deviation` function tests the function against a list with larger deviations from the mean, expecting a mean absolute deviation of approximately 1.5.

By running this code, you can verify that the function correctly calculates the mean absolute deviation for various input scenarios. Adjust the test cases in the `TestMeanAbsoluteDeviation` class as needed to cover additional scenarios and ensure the function's correctness.
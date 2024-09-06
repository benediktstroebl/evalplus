Here's a Python script with a self-contained function that solves the problem you've described, along with a few tests to validate its correctness:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.)

    def test_no_deviation(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4., 5.]), 0.)

    def test_large_deviation(self):
        self.assertEqual(mean_absolute_deviation([0., 1., 2., 3., 4.]), 3.)

if __name__ == '__main__':
    unittest.main()
```
This script provides a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It employs the `numpy` library to operate on arrays and perform calculations efficiently.

The `TestMeanAbsoluteDeviation` class derives from `unittest.TestCase` and bundles a few test cases to validate the behavior of the function:
- `test_basic`: This tests the function with a list of numbers where the mean absolute deviation can be verified easily.
- `test_no_deviation`: This tests the function with a list of numbers where the mean absolute deviation is zero.
- `test_large_deviation`: This tests the function with a list of numbers where the mean absolute deviation is expected to be larger.
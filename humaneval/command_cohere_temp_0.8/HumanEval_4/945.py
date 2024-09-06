Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_single_number(self):
        self.assertEqual(mean_absolute_deviation([1.0]), 0)

    def test_mean_absolute_deviation_two_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0]), 1.0)

    def test_mean_absolute_deviation_three_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0]), 1.0)

    def test_mean_absolute_deviation_four_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

if __name__ == '__main__':
    unittest.main()
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It uses the `numpy` library to operate on the input list and calculate the MAD.

The `unittest` module is used to test the function with different input lists to ensure it returns the expected results. You can run this script, and the test cases will verify the correctness of the `mean_absolute_deviation` function.
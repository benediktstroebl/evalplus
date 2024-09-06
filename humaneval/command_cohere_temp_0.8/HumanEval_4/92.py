Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)
    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.)
    def test_large_deviations(self):
        self.assertEqual(mean_absolute_deviation([5., 10., 15., 20.]), 5.0)

if __name__ == '__main__':
    unittest.main()
```
This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It utilizes the `numpy` library to operate on arrays and perform calculations efficiently. The function takes a list of numbers as input and returns the mean absolute deviation as a float. 

The script also includes a test class `TestMeanAbsoluteDeviation` that verifies the correctness of the function against a few test cases, including a basic test with a list of integers, an empty list test, and a test with large deviations. 

To run the tests, execute the script directly (`python ScriptName.py`) or use a testing framework like `pytest` if it is installed in your environment.
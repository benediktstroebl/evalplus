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
        self.assertEqual(mean_absolute_deviation([5., 7.,  9., 11.]), 5.0/4)

if __name__ == '__main__':
    unittest.main()
```
This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function uses the NumPy library to perform the calculations.

The `test_mean_absolute_deviation` class runs a series of tests on the function to ensure that it behaves as expected. Specifically, it tests the function with a basic example, an empty list, and a list with large deviations. 

The `unittest.main()` function is used to discover and run the tests.  This way, running the script will automatically execute the tests and report any failures. 

You can use this script as a starting point to calculate the mean absolute deviation of a list of numbers.  You can do this by calling the `mean_absolute_deviation()` function with a list of numbers as an argument.  This function will return the mean absolute deviation of the provided list.
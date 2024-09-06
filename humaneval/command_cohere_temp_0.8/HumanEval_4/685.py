Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_basic(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)

    def test_mean_absolute_deviation_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

    def test_mean_absolute_deviation_negative_values(self):
        self.assertEqual(mean_absolute_deviation([10., -5., 7., -3.]), 11.0)

if __name__ == '__main__':
    unittest.main()
```
This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It uses the numpy library to operate on the input list and calculate the deviation.

The script also includes a set of unit tests that are defined in the `TestMeanAbsoluteDeviation` class. These tests verify that the `mean_absolute_deviation` function behaves as expected. In particular, it checks the function's behavior on basic usage, with an empty list, and with negative values included in the list. 

Finally, the `if __name__ == '__main__':` block at the end of the script is used to run the unit tests when the script is executed directly. 
It can be run as a standalone script or integrated into a larger project.
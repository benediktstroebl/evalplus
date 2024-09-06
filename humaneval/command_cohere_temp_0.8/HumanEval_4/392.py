Here's a Python script with a self-contained function that solves the problem you've outlined, along with a few tests to validate its correctness:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_with_list(self):
        """ Test function with a list of positive and negative numbers."""
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    def test_mean_absolute_deviation_with_deviated_list(self):
        """ Test function with a list of numbers where every element is deviated from the mean."""
        self.assertEqual(mean_absolute_deviation([10.0, 20.0, 30.0, 40.0]) , 10.0)

    def test_mean_absolute_deviation_with_single_number(self):
        """ Test function with a single input."""
        self.assertEqual(mean_absolute_deviation([10.0]), 0.0)

    def test_mean_absolute_deviation_with_empty_list(self):
        """ Test function with an empty list."""
        self.assertEqual(mean_absolute_deviation([]), 0.0)

if __name__ == '__main__':
    unittest.main()
```
This script includes:
1. The `mean_absolute_deviation` function: Calculates the mean absolute deviation of a list of numbers.
2. Unit tests: Four different tests to validate the function's behavior on various input scenarios.

The `unittest.main()` function is used to discover and run the tests.  Running this script (e.g., by typing `python test_mean_absolute_deviation.py` at the command line)
will execute the tests and report any failures, assuring us that the `mean_absolute_deviation` function behaves as expected.
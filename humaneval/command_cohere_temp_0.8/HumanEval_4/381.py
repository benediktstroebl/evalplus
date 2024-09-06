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
    def test_large_values(self):
        self.assertAlmostEqual(mean_absolute_deviation([10., 9., 8., 7.]), 1.0)

if __name__ == '__main__':
    unittest.main()
```
This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It utilizes the `numpy` library to perform the necessary calculations. 

The function takes a list of numbers as input and returns the mean absolute deviation of the numbers in the list. The mean absolute deviation is calculated by finding the average of the absolute differences between each number and the mean of the numbers. 

The script also includes a set of unit tests for the `mean_absolute_deviation` function to verify its correctness. The tests check for scenarios such as a basic list of numbers, an empty list, and large value lists. 

To run the tests, the script uses the `unittest` module. If you run this script, it will automatically execute the tests and report any failures or errors. 

Overall, this Python script provides an effective way to compute the mean absolute deviation of a list of numbers, and the included tests ensure the function's reliability.  Any feedback on this solution is welcome. Let me know if you would like to have any additional clarifications or if you'd like to proceed with other problems.
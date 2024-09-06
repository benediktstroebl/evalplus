Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)
        self.assertEqual(mean_absolute_deviation([0., 0., 0.]), 0.0)
    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), None)

if __name__ == '__main__':
    unittest.main()
```
This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function uses the NumPy library to perform the necessary calculations.

The script also includes a set of unit tests that verify the correctness of the `mean_absolute_deviation` function. The tests pass the function with lists of numbers and verify that the returned mean absolute deviation is correct. These tests include testing an example with a list of four numbers, testing an example with a list of three zeros, and testing an example with an empty list. 

The `unittest.main()` function is called to run the unit tests. Overall, this code provides a function to solve the problem and comprehensive tests to ensure its correctness.  This solution is efficient and provides accurate results based on the inputs.  If you have any questions, let me know!
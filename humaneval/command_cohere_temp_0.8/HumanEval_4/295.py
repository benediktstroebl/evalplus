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
    def test_no_deviation(self):
        self.assertEqual(mean_absolute_deviation([1., 1., 1., 1.]), 0.)
    def test_large_deviation(self):
        self.assertAlmostEqual(mean_absolute_deviation([0., 1., 2., 3., 4., 5.]), 1.5, places=2)

if __name__ == '__main__':
    unittest.main()
```
This script incorporates the `mean_absolute_deviation` function, which is designed to calculate the mean absolute deviation of a list of numbers. It achieves this by employing `numpy` to compute the absolute differences between each element of the list and the mean of the list, and then calculating the average of these absolute differences. 

The code includes a set of unit tests, defined in the `TestMeanAbsoluteDeviation` class, which serve to validate the correctness of the `mean_absolute_deviation` function. These tests check various scenarios, including a basic test case, a case with no deviation, and a scenario involving large deviations. 

Finally, the `unittest.main()` function is invoked to execute the unit tests. 

This script encapsulates a function to solve the problem statement and incorporates tests to ensure its correctness.
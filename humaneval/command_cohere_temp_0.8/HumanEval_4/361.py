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
    def test_mean_absolute_deviation_large_dataset(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        self.assertEqual(mean_absolute_deviation(numbers), 2.0)

if __name__ == '__main__':
    unittest.main()
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It utilizes the `numpy` library to operate on the input list and calculate the deviation.

The script also includes a set of unit tests for the `mean_absolute_deviation` function. The tests are defined as methods within the `TestMeanAbsoluteDeviation` class, which is derived from `unittest.TestCase`. 

If you run this script, the unittest framework executes the test methods `test_mean_absolute_deviation` and `test_mean_absolute_deviation_large_dataset`, ensuring that the function `mean_absolute_deviation` produces the expected results for different scenarios.
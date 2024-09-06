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

    def test_mean_absolute_deviation_with_negative_values(self):
        self.assertEqual(mean_absolute_deviation([1., -2., 3., -4.]), 2.0)

    def test_mean_absolute_deviation_with_single_value(self):
        self.assertEqual(mean_absolute_deviation([10.0]), 0.0)

    def test_mean_absolute_deviation_with_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

if __name__ == '__main__':
    unittest.main()
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It uses the `numpy` library to operate on arrays and perform calculations efficiently. The function is then tested comprehensively using a set of test cases in the `TestMeanAbsoluteDeviation` class that covers various scenarios, such as basic tests, negative values, single value, and an empty list.

The `unittest` framework is used to organize and run the tests, and the `if __name__ == '__main__':` block ensures that the tests are executed only when the script is run directly and not when it's imported elsewhere.
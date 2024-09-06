Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_with_list_of_numbers(self):
        numbers = [1., 2., 3., 4.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

    def test_mean_absolute_deviation_with_empty_list(self):
        numbers = []
        with self.assertRaises(ValueError):
            mean_absolute_deviation(numbers)

    def test_mean_absolute_deviation_with_single_number(self):
        numbers = [5.]
        self.assertEqual(mean_absolute_deviation(numbers), 0.)

if __name__ == '__main__':
    unittest.main()
```

This script includes the `mean_absolute_deviation` function, which calculates the mean absolute deviation of a list of numbers, as described in the problem statement. It also includes a `unittest` module to test the function with different inputs.

The `test_mean_absolute_deviation_with_list_of_numbers` tests assert that the function returns 1.0 when passed the example list of numbers from the docstring [1.0, 2.0, 3.0, 4.0]. The `test_mean_absolute_deviation_with_empty_list` test asserts that the function raises a `ValueError` when an empty list is passed. The `test_mean_absolute_deviation_with_single_number`  test asserts that the function returns 0. when passed a list containing a single value.
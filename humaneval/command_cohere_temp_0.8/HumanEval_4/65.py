Here is a Python script with a self-contained function that solves the problem of calculating the mean absolute deviation of a list of numbers and passes corresponding tests:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_with_list_of_numbers(self):
        numbers = [1., 2., 3., 4.]
        self.assertAlmostEqual(mean_absolute_deviation(numbers), 1.0)

    def test_mean_absolute_deviation_with_list_of_strings(self):
        self.assertRaises(TypeError, mean_absolute_deviation, ['a', 'b', 'c'])

if __name__ == '__main__':
    unittest.main()
```
This script incorporates the NumPy library to efficiently handle array operations. The `mean_absolute_deviation()` function accepts a list of numbers, converts it to a NumPy array, and calculates the mean absolute deviation using NumPy's `mean()` function.

The `test_mean_absolute_deviation_with_list_of_numbers` function verifies that the calculated mean absolute deviation matches the expected value of 1.0 for a sample list of numbers.

Furthermore, the `test_mean_absolute_deviation_with_list_of_strings` function ensures that the function raises a `TypeError` when a list of strings is provided, as the function expects a list of numbers.

The `unittest.main()` call enables the running of the tests when the script is executed directly.
Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_single_number(self):
        self.assertEqual(mean_absolute_deviation([1.0]), 0)

    def test_mean_absolute_deviation_list_of_two_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0]), 1.0)

    def test_mean_absolute_deviation_list_of_three_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0]), 1.0)

    def test_mean_absolute_deviation_list_of_four_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

if __name__ == '__main__':
    unittest.main()
```

Let's break down the code:
- The function 'mean_absolute_deviation' accepts a list of numbers as input and utilizes NumPy to calculate the mean absolute deviation of the provided list of numbers.
- 'unittest.TestCase' is imported to facilitate unit testing.
- The 'test_mean_absolute_deviation_single_number' function tries a simple case with a single input number and expects the result to be zero.
- The 'test_mean_absolute_deviation_list_of_two_numbers' and analogous functions test cases for lists of increasing sizes, asserting that the mean absolute deviation is 1.

The `unittest.main()` function is invoked to execute the unit tests.  This approach provides a robust test suite to validate the 'mean_absolute_deviation' function.
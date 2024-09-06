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

    def test_mean_absolute_deviation_with_list_of_negative_numbers(self):
        numbers = [-1, -2, -3, -4]
        mean_deviation = mean_absolute_deviation(numbers)
        expected_result = np.mean(np.abs(np.array(numbers)))
        self.assertEqual(mean_deviation, expected_result)

if __name__ == '__main__':
    unittest.main()
```

This script includes the `mean_absolute_deviation` function, which calculates the mean absolute deviation of a list of numbers. It also includes a `unittest` module to test the function with different inputs.

The `mean_absolute_deviation` function calculates the mean absolute deviation of a list of numbers, defined as the average absolute difference between each element and the mean of the list. 

The `unittest` module contains tests for the `mean_absolute_deviation` function. The `test_mean_absolute_deviation_with_list_of_numbers` test checks that the function returns 1.0 when passed a list of numbers [1.0, 2.0, 3.0, 4.0]. The `test_mean_absolute_deviation_with_empty_list` test checks if the function raises a `ValueError` error when an empty list is passed in. The `test_mean_absolute_deviation_with_list_of_negative_numbers` test assesses whether the output aligns with the expected result when the function is provided a list of negative numbers. 

The `if __name__ == '__main__':` line ensures that the `unittest` module runs when this script is executed directly.  It can be when imported as a module, but these tests will not run.
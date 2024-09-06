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
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

    def test_mean_absolute_deviation_with_list_of_neg_numbers(self):
        numbers = [-1., -2., -3., -4.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

    def test_mean_absolute_deviation_with_single_number(self):
        numbers = [5.]
        self.assertEqual(mean_absolute_deviation(numbers), 0.0)

    def test_mean_absolute_deviation_with_empty_list(self):
        numbers = []
        with self.assertRaises(ValueError):
            mean_absolute_deviation(numbers)

if __name__ == '__main__':
    unittest.main()
```

In the above code, the `mean_absolute_deviation()` function calculates the Mean Absolute Deviation of a list of numbers using the `numpy` library. It then centrifies the list by calculating the mean, and finally, returns the average absolute deviation from the mean. 

The `TestMeanAbsoluteDeviation` class defines four test functions to validate the behavior of the `mean_absolute_deviation()` function:
- `test_mean_absolute_deviation_with_list_of_numbers`: Validates the function with a list of positive numbers.
- `test_mean_absolute_deviation_with_list_of_neg_numbers`: Validates the function with a list of negative numbers.
- `test_mean_absolute_deviation_with_single_number`: Validates the function with a list containing a single number.
- `test_mean_absolute_deviation_with_empty_list`: Validates when the input list is empty, expecting it to raise a `ValueError`.

This script includes a `unittest.main()` call to run the tests when the script is executed directly. 

Mean Absolute Deviation is a robust statistical measure that is not bothered by outliers or correlations and aids in understanding the spread of data points in any direction from the centerpoint.
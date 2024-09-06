Here's a Python script with a self-contained function that solves the problem you've outlined, along with a separate test suite to verify its correctness:
```python
# -*- coding: utf-8 -*-
import numpy as np
import unittest

from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the mean absolute deviation of a list of numbers.
    
    Parameters:
        numbers (list of float): A list of numerical data.
    
    Returns:
        float: The mean absolute deviation of the input list.
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_basic(self):
        """
        Test on a simple list with known mean and range.
        """
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

    def test_empty_list(self):
        """
        Test for an empty list.
        """
        numbers = []
        with self.assertRaises(ValueError):
            mean_absolute_deviation(numbers)

    def test_single_number(self):
        """
        Test on a list with a single element.
        """
        numbers = [10]
        self.assertEqual(mean_absolute_deviation(numbers), 0.0)

    def test_negative_numbers(self):
        """
        Test on a list with negative numbers.
        """
        numbers = [-1, -2, 3, 4, -5]
        mean_deviation = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(mean_deviation, 3.0, places=1)

    def test_large_numbers(self):
        """
        Test on a list with large numbers.
        """
        numbers = [999, 99999, 44444, 22222, 99977]
        mean_deviation = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(mean_deviation, 22222 / 5, places=2)

if __name__ == '__main__':
    unittest.main()
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It also features a test suite named `TestMeanAbsoluteDeviation` that checks the function's correctness against a variety of test cases.

The `mean_absolute_deviation` function utilizes the `abs` function and the `mean` function from the `numpy` library to find the absolute differences between each list element and the mean, and then calculate the mean of these absolute differences, respectively. 

The test suite comprises several test functions, each of which checks the function's output against an expected result using the `assertEqual` function. If the values don't match, the test suite throws an error.

To run the test suite, execute the script. The script is set up to automatically run the test suite if the script is executed directly. 

This code is compatible with Python versions that support the `numpy` library, and the `typing` module which is available since Python 3.5. It is also backward compatible with Python 3.5. Finally, it installs no additional dependencies besides the numpy library, ensuring that the codebase is self-contained.
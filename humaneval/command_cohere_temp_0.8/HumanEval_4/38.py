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
        self.assertEqual(mean_absolute_deviation(numbers), 3.0)

if __name__ == '__main__':
    unittest.main()
```

Let's break down the code:
1. We import the necessary libraries: `typing` for type hints, `numpy` for numerical operations, and `unittest` for creating test cases.
2. The `mean_absolute_deviation` function calculates the mean absolute deviation of a list of numbers. It first converts the input list to a numpy array, then calculates the mean of the absolute differences between each element and the mean of the array.
3. The `TestMeanAbsoluteDeviation` class defines three test methods. 
4. `test_mean_absolute_deviation_with_list_of_numbers`: This tests the function with a list of numbers and verifies that the result is correct.
5. `test_mean_absolute_deviation_with_empty_list`: This tests the function with an empty list and verifies that it raises a `ValueError` as the input data is not sufficient.
6. `test_mean_absolute_deviation_with_list_of_negative_numbers`: This tests the function with a list of negative numbers and verifies that the result is correct.

The script and function will calculate the Mean Absolute Deviation property for any list of numbers provided as an input. 

This property is an important concept in data analysis, helping to understand the spread of data points from the mean.
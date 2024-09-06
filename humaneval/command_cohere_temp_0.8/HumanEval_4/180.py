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
    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.)
    def test_large_deviations(self):
        self.assertEqual(mean_absolute_deviation([5., 7.,  9., 11.]), 3.0)

if __name__ == '__main__':
    unittest.main()
```

Let's break down the code:
- The script includes the necessary imports, including `List` from Python's `typing` module, `numpy` for numerical operations, and `unittest` for creating test cases.
- The `mean_absolute_deviation(numbers: List[float]) -> float:` function calculates the mean absolute deviation of a list of numbers. It uses `numpy` to convert the input list to a numpy array, calculates the mean of the array, and then calculates the absolute difference between each element of the array and the mean. It then returns the average of these absolute differences, which is the mean absolute deviation.
- The `TestMeanAbsoluteDeviation` class inherits from `unittest.TestCase`, enabling the creation of test methods that start with the prefix `test_`. 
- The `test_basic` method tests the function with a simple list of numbers and asserts that the mean absolute deviation is correct.
- The `test_empty_list` method tests the function with an empty list, and asserts that the result is 0. since the deviation is taken from the mean, which is also 0 for an empty list.
- The `test_large_deviations` method tests the function with a list of numbers where each number is several degrees away from the mean. It asserts that the mean absolute deviation is correct.
- Finally, the `if __name__ == '__main__':` block runs the tests when the script is executed directly. 

This script provides a self-contained function to calculate the mean absolute deviation and incorporates corresponding tests to validate the correctness of the implementation.
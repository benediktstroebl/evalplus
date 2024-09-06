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
    def test_ EmptyList(self):
        with self.assertRaises(ValueError):
            mean_absolute_deviation([])
    def test_LargeList(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]), 1.0)

if __name__ == '__main__':
    unittest.main()
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function uses the NumPy library to perform the calculations with less code and the `unittest` module to test the functionality of the function. 

The `TestMeanAbsoluteDeviation` class derives from `unittest.TestCase` and contains three test methods. `test_basic` tests the function with a simple list of numbers, `test_empty_list` checks if the function raises a `ValueError` for an empty list, and `test_large_list` verifies the function works correctly with a larger list of numbers. 

Finally, the `if __name__ == '__main__':` block at the end of the script enables the `unittest.main()` function to run the test suite when this script is executed directly. 

This script provides a self-contained solution to the problem and also includes tests to verify the correctness of the implementation.
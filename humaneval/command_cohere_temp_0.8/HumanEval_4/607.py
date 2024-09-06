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
        self.assertEqual(mean_absolute_deviation([5., 10., 15., 20.]), 5.0)

if __name__ == '__main__':
    unittest.main()
```
This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function takes a list of floats as input and returns the mean absolute deviation as a float. 

The script also includes a set of unit tests for the `mean_absolute_deviation` function. These tests verify that the function correctly calculates the mean absolute deviation for various input lists, including empty lists and lists with large deviations. 

The `unittest` module is used to define and run the tests. The `TestCase` class is used to define each individual test case, and `assertEqual` is used to verify that the output of the `mean_absolute_deviation` function is correct for a given input. 

When you run the script, the `unittest` framework executes each test case separately and reports any failures or errors. If all tests pass, the output will indicate that everything is okay. 

This code demonstrates how to properly test numerical code in Python and ensures that the `mean_absolute_deviation` function operates as expected, encouraging code reliability and robustness. 

I hope this helps! Let me know if you have any other questions.
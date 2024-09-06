Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)
        self.assertEqual(mean_absolute_deviation([0., 0., 0.]), 0.0)
    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)
    def test_single_number(self):
        self.assertEqual(mean_absolute_deviation([1.0]), 0.0)

if __name__ == '__main__':
    unittest.main()
```

This script includes the `mean_absolute_deviation` function, which calculates the mean absolute deviation of the list of numbers it receives as input. It also includes a `test_mean_absolute_deviation` function that runs a test on the `mean_absolute_deviation` function with three different inputs. 

The `TestMeanAbsoluteDeviation` class includes three test functions:
- `test_mean_absolute_deviation`: This function passes two lists of numerical values as input and checks if the output of the `mean_absolute_deviation` function is correct. These inputs include a list of numbers with a mean of 1 and a list of zeros with a mean of 0.
- `test_empty_list`: This function passes an empty list as input to see if the function handles it correctly and returns 0. 
- `test_single_number`: This function tests the function's output when the input list contains only one number, ensuring the function returns 0. 

This code uses the `unittest` module to run the test functions automatically and demonstrate that the `mean_absolute_deviation` function behaves as expected. 

When you run the script, the unittest framework will run the test methods. You will see the test results, which will indicate zero failed tests (and zero skipped tests) if the `mean_absolute_deviation` function calculates the mean absolute deviation correctly.
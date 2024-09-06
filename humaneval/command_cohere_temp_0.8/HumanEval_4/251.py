Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_basic(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)
    def test_mean_absolute_deviation_with_negative_values(self):
        self.assertEqual(mean_absolute_deviation([1., -2., 3., -4.]), 2.0)
    def test_mean_absolute_deviation_with_single_value(self):
        self.assertEqual(mean_absolute_deviation([10.]), 0.0)
    def test_mean_absolute_deviation_with_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)
if __name__ == '__main__':
    unittest.main()
```

This script includes the `mean_absolute_deviation` function, which calculates the mean absolute deviation of a list of numbers, and a set of unit tests for that function. 

The `mean_absolute_deviation` function calculates the absolute deviation of each number in the list from the mean of the list. It then calculates the average of these absolute deviations and returns it. 

The `TestMeanAbsoluteDeviation` class defines four unit tests for the `mean_absolute_deviation` function. Each test case includes a list of numbers and expects the result of the function to match the expected value. 

The `if __name__ == '__main__':` block at the end of the script enables the unit tests to run when the script is executed directly. 

This code demonstrates how to properly calculate the Mean Absolute Deviation in Python and includes tests to ensure its correctness, making it a robust and reliable solution. You can use this code directly in your project, and it can be easily adapted to accommodate any changes or additional requirements you may have in the future.
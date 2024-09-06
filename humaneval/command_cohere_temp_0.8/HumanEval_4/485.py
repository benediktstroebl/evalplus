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
- The `mean_absolute_deviation()` function uses numpy to calculate the mean of the absolute deviations of the numbers in the input list from the mean of the list. 
- The `TestMeanAbsoluteDeviation` class imports the `unittest` module and defines four test methods that test the `mean_absolute_deviation()` function with various input list lengths.
- If the `unittest.main()` function is executed, the test suite is run. 

This code demonstrates how to appropriately utilize numpy to compute statistics related to lists of numbers and how to construct tests using the `unittest` module to ensure that the statistical computation function operates as anticipated.
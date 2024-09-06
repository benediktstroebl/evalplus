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

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It uses the `numpy` library to perform the calculations, returning the result as a float. 

The script also includes a unit test class `TestMeanAbsoluteDeviation` that checks the functionality of the `mean_absolute_deviation` function. It comprises several test methods that verify the function's behavior for different input scenarios. When the script is executed, the `unittest.main()` function runs all the test methods to ensure the correctness of the `mean_absolute_deviation` function.
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
- The Python script includes the necessary imports, specifically `numpy` for numerical operations and `unittest` for creating test cases.
- The `mean_absolute_deviation` function calculates the mean absolute deviation of a list of numbers. It uses `numpy` to convert the input list to an array, calculates the mean of the array, and then calculates the absolute difference between each element of the array and the mean. The mean of these absolute differences is the desired Mean Absolute Deviation.
- The `unittest.TestCase` class is used to define test cases for the `mean_absolute_deviation` function. Each test case is defined as a method within the class, and the `self.assertEqual()` method is used to check if the actual output of the function matches the expected output for each test case.
- The `if __name__ == '__main__':` block runs the tests when the script is executed directly.

The script demonstrates how to effectively utilize `numpy` for numerical computations and `unittest` for creating test cases to ensure the correctness of the implemented function. 

This way, the code chunk is now self-contained, and it can be executed independently to assess the functionality of the `mean_absolute_deviation` function with the included test cases. 

Additionally, this code can serve as a foundation for more testing scenarios and exploring additional statistical measures in the future.
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

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It uses the `numpy` library to operate on arrays and perform calculations efficiently. The function is then tested through a series of unit tests that cover different scenarios, from a list with a single number to lists of increasing size. 

The `unittest` module is used to define test cases and run the tests when the script is executed directly, ensuring the function behaves as expected and helping to maintain the code over time. 

To run this code, you'll need to have the `numpy` library installed. Usually, you can install it using the command `pip install numpy`. 

Additionally, ensure you are running a compatible Python version that supports type hints and the `numpy` library, such as Python 3.6 or later. 

This code encapsulates the solution to the problem in a self-contained manner, providing both the function to calculate the mean absolute deviation and the unit tests to ensure its correctness.
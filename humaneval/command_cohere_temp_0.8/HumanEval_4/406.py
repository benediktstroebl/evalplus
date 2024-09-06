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
1. We import the necessary libraries: `typing` for type hints, `numpy` for numerical operations, and `unittest` for creating tests.
2. The `mean_absolute_deviation` function calculates the mean absolute deviation of a list of numbers. It first converts the input list to a numpy array, then calculates the mean of the absolute differences between each element and the mean of the array. 
3. The `TestMeanAbsoluteDeviation` class inherits from `unittest.TestCase` and defines four test methods. Each method tests the `mean_absolute_deviation` function with different input lists and confirms that the result is as expected.
4. Finally, `unittest.main()` is called to discover and run the test cases. 

This code demonstrates the use of typed Python with Numpy to compute the mean absolute deviation in a tested manner.
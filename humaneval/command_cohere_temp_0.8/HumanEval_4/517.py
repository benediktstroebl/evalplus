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

    def test_mean_absolute_deviation_two_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0]), 1.0)

    def test_mean_absolute_deviation_three_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0]), 1.0)

    def test_mean_absolute_deviation_four_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

if __name__ == '__main__':
    unittest.main()
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It uses the `numpy` library to perform the calculations. 

The `unittest` module is also used to include tests that check the function's behavior on simple cases like lists of one, two, three, and four numbers.

The `TestMeanAbsoluteDeviation` class subclasses `unittest.TestCase` and defines several test methods that use `self.assertEqual()` to check if the function returns the expected results for specific inputs. You can use this script as a starting point and modify it to suit your needs. 

To run the test, this script uses `unittest.main()` which executes the test when the script is run directly. If you intend to use this script in a larger context, you might want to use pytest for more flexible and readable test writing.
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
        self.assertEqual(mean_absolute_deviation([]), None)

if __name__ == '__main__':
    unittest.main()
```

Let's break down the code step by step:
- The script includes necessary imports for typing, numpy, and testing libraries.
- The `mean_absolute_deviation` function calculates the mean absolute deviation of a list of numbers. It uses `numpy` for efficient numerical operations. 

Here is a brief overview of the function:
- The function takes a list of numbers as input.
- It converts the list to a numpy array for easier mathematical operations.
- It calculates the mean of the array.
- It subtracts the mean from each number and calculates the absolute value to get the deviation.
- It calculates the mean of these deviations.
- Finally, it returns the mean of the absolute deviations.

The testing framework in Python is used to ensure the function behaves as expected:
- The `TestMeanAbsoluteDeviation` class inherits from `unittest.TestCase`.
- Each test is defined as a method within this class, starting with the prefix 'test'.
- In this case, two tests are defined:
  - `test_mean_absolute_deviation`: This tests the functionality of the `mean_absolute_deviation` function with two specific cases.
  - `test_empty_list`: This tests the function's behavior when an empty list is passed as input. 

The `unittest.main()` function is necessary to discover and run the tests. 

The script is designed to be executed directly (as opposed to being imported as a module) so that the tests will run automatically. 

When you run the script, Python's unittest framework will execute each test method, and an output will be displayed indicating whether the tests passed or failed.
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

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It uses the `numpy` library to handle numerical operations and the `typing` module to specify the type of the input parameter.

The `unittest` module is used to define and run tests. The `TestMeanAbsoluteDeviation` class inherits from `unittest.TestCase` and defines individual test methods that test the function's behavior for different input scenarios. 

The `if __name__ == '__main__':` block at the end of the script invokes `unittest.main()` to run the tests when the script is executed directly.

The script is self-contained and can be executed independently to test the `mean_absolute_deviation` function and verify that it meets the specified requirements. You can run the script in a Python environment or IDE that supports unittest functionality.
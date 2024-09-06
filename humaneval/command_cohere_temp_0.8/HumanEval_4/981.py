Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)
    def test_single_number(self):
        self.assertEqual(mean_absolute_deviation([10.0]), 0.0)
    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)
    def test_large_list(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        self.assertAlmostEqual(mean_absolute_deviation(numbers), 1.0)

if __name__ == '__main__':
    unittest.main()
```

This script includes a function called `mean_absolute_deviation` designed to calculate the mean absolute deviation of a list of numbers. The function utilizes the `numpy` library to perform the necessary calculations, including vectorized operations on the input list. The result is returned as a float. 

The script also includes a set of unit tests, defined as a `TestMeanAbsoluteDeviation` class that exercises the `mean_absolute_deviation` function across various scenarios:
1. `test_basic()`: validates the function's behavior with a simple list of numbers [1., 2., 3., 4.], expecting a result of 1.0.
2. `test_single_number()`: confirms that the function handles a list with a single number (10.0) correctly, resulting in zero deviation.
3. `test_empty_list()`: verifies that the function deals with an empty list efficiently, returning zero as well.
4. `test_large_list()`: assesses the function using a larger list of integers, [1.0, 2.0, 3.0, ..., 10.0], expecting a roughly equal result to 1.0.

Additionally, the script employs the `unittest.main()` function to execute these tests sequentially upon script execution. 

Note that this script utilizes the `numpy` library and incorporates type hints with the `typing` module for better clarity and functionality.
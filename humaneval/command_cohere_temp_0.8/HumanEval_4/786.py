Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_with_list_of_numbers(self):
        numbers = [1., 2., 3., 4.]
        self.assertAlmostEqual(mean_absolute_deviation(numbers), 1.0)

    def test_mean_absolute_deviation_with_empty_list(self):
        numbers = []
        with self.assertRaises(ValueError):
            mean_absolute_deviation(numbers)

    def test_mean_absolute_deviation_with_single_number(self):
        numbers = [5.]
        self.assertEqual(mean_absolute_deviation(numbers), 0.)

if __name__ == '__main__':
    unittest.main()
```
This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It uses the `numpy` library to perform the necessary calculations, including vectorized operations and mean calculation.

The script also includes a set of unit tests for the function, which are defined in the `TestMeanAbsoluteDeviation` class. These tests cover different scenarios, including a standard list of numbers, an empty list, and a single number. 

The `unittest.main()` function is used to discover and run the tests. Thus, when the script is executed directly (rather than being imported as a module), the tests will automatically run. 

The `assertAlmostEqual` and `assertEqual` methods are used to compare the expected and actual results, allowing for a tolerance margin in the comparisons.
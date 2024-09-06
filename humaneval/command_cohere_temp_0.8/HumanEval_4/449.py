Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

And here is a markdown code block with corresponding test code:
```python
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        numbers = [1., 2., 3., 4.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

    def test_mean_absolute_deviation_with_negative_values(self):
        numbers = [1., -2., 3., -4.]
        self.assertEqual(mean_absolute_deviation(numbers), 2.0)

    def test_mean_absolute_deviation_with_single_value(self):
        numbers = [5.]
        self.assertEqual(mean_absolute_deviation(numbers), 0.0)

    def test_mean_absolute_deviation_with_empty_list(self):
        numbers = []
        with self.assertRaises(ValueError):
            mean_absolute_deviation(numbers)
```

This script and tests verify the functionality of the `mean_absolute_deviation` function. It accepts a list of numbers and returns the mean absolute deviation, which is the average of the absolute differences between each element and the mean of the list. The tests check for correctness in various scenarios, including positive and negative values as well as edge cases like an empty list.

The `numpy` library is used for numerical operations for efficiency and handling large datasets. Using the `unittest` module, the test class constructs test cases to cover different scenarios.
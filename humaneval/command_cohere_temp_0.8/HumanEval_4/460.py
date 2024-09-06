Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

And here is a markdown code block with corresponding test data and expected output:
```python
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        numbers = [1., 2., 3., 4.]
        mean_dev = mean_absolute_deviation(numbers)
        self.assertEqual(mean_dev, 1.0)

    def test_mean_absolute_deviation_with_negative_values(self):
        numbers = [-1., 0., 2., 3.]
        mean_dev = mean_absolute_deviation(numbers)
        self.assertEqual(mean_dev, 1.0)

    def test_mean_absolute_deviation_with_single_value(self):
        numbers = [5.]
        mean_dev = mean_absolute_deviation(numbers)
        self.assertEqual(mean_dev, 0.)

    def test_mean_absolute_deviation_with_empty_list(self):
        numbers = []
        with self.assertRaises(ValueError):
            mean_absolute_deviation(numbers)
```

You can run this test suite by executing `python test_mean_absolute_deviation.py` in your command line. 

This script uses the `numpy` library to calculate the mean and absolute deviations, as well as the `unittest` library to test the functionality of the `mean_absolute_deviation` function. 

The test suite contains four test cases:
1. Test case `test_mean_absolute_deviation` checks if the function returns 1.0 when the input list [1., 2., 3., 4.] is passed.
2. Test case `test_mean_absolute_deviation_with_negative_values` verifies if the function returns 1.0 when the list [-1., 0., 2., 3.] is passed.
3. Test case `test_mean_absolute_deviation_with_single_value` checks if the function returns 0. when the list [5.] is passed.
4. Finally, `test_mean_absolute_deviation_with_empty_list` verifies that the function raises a `ValueError` when an empty list is passed. 

These test cases cover multiple scenarios and edge cases, ensuring that the `mean_absolute_deviation` function behaves as expected.
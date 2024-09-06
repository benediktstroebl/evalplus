Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_basic(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)
    def test_mean_absolute_deviation_with_negative_values(self):
        self.assertEqual(mean_absolute_deviation([1., -2., 3., -4.]), 2.0)
    def test_mean_absolute_deviation_with_single_value(self):
        self.assertEqual(mean_absolute_deviation([10.]), 0.0)
    def test_mean_absolute_deviation_with_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

if __name__ == '__main__':
    unittest.main()
```

This script includes the `mean_absolute_deviation` function, which calculates the mean absolute deviation of a list of numbers. It also includes a `unittest` class, `TestMeanAbsoluteDeviation`, which contains several test methods that check the function's behavior against expected outputs for different inputs. 

The `test_mean_absolute_deviation_basic` method checks the function's output for a list of numbers [1., 2., 3., 4.], which should result in a mean absolute deviation of 1.0; `test_mean_absolute_deviation_with_negative_values` verifies the function's output for a list [1., -2., 3., -4.], expecting a mean absolute deviation of 2.0; `test_mean_absolute_deviation_with_single_value` checks if the function outputs 0.0 for an input list [10.]; and `test_mean_absolute_deviation_with_empty_list` verifies if the function's output is 0.0 for an empty list. 

Finally, `unittest.main()` is called to run all the test methods.
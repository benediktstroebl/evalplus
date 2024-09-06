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

This script includes the `mean_absolute_deviation` function from the original prompt and adds a `unittest` class, `TestMeanAbsoluteDeviation`, with test methods that cover various scenarios. The `unittest.main()` call runs the tests when the script is executed directly.
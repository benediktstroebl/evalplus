Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
    def test_mean_absolute_deviation_large_dataset(self):
        numbers = [1 for _ in range(10000)]
        self.assertAlmostEqual(mean_absolute_deviation(numbers), 0.0, places=1)

if __name__ == '__main__':
    unittest.main()
```

In the above code, the `mean_absolute_deviation()` function takes a list of numbers as input and uses `numpy` to calculate the mean absolute deviation. The `TestMeanAbsoluteDeviation` class inherits from `unittest.TestCase` and contains two test methods to verify the correctness of the `mean_absolute_deviation()` function. The `test_mean_absolute_deviation()` method tests the function with two sample datasets, and `test_mean_absolute_deviation_large_dataset()` tests the function with a larger dataset. Finally, `unittest.main()` is called to discover and run the test cases.  This script guarantees that the `mean_absolute_deviation()` function computes the Mean Absolute Deviation properly.
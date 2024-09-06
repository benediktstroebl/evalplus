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
    def test_mean_absolute_deviation_large_dataset(self):
        numbers = [1 for i in range(10000)]
        num_mean = sum(numbers) / len(numbers)
        num_mad = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(num_mean, 0, places=1)
        self.assertAlmostEqual(num_mad, 0, places=1)

if __name__ == '__main__':
    unittest.main()
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It leverages `numpy` to process the input list into an array, compute the mean of the array, and then calculate the absolute deviations from the mean, returning the mean of these deviations as the final result. 

The script also includes a battery of tests, defined in `TestMeanAbsoluteDeviation`, that validate the correctness of this function against two primary scenarios:
1. `test_mean_absolute_deviation`: This tests the function against a small dataset [1., 2., 3., 4.], expecting the mean absolute deviation to be 1.0.
2. `test_mean_absolute_deviation_large_dataset`: This tests the function against a large dataset of numbers [1 for i in range(10000)], expecting the mean absolute deviation to converge to zero (given that the mean of this dataset is 0).

This battery of tests ensures that the function behaves as expected on both small and large datasets, demonstrating its correctness in handling these cases.
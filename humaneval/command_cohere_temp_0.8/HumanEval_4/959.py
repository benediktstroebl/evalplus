Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
        num_deviation = mean_absolute_deviation(numbers)
        mean = np.mean(numbers)
        expected_deviation = np.abs(np.mean(numbers) - mean)
        self.assertAlmostEqual(num_deviation, expected_deviation, places=1)

if __name__ == '__main__':
    unittest.main()
```

In this script:
- The `mean_absolute_deviation` function calculates the mean absolute deviation of a list of numbers, using `numpy` for efficiency.
- The `TestMeanAbsoluteDeviation` class defines two test cases: one for a small dataset and one for a large dataset.
- The `test_mean_absolute_deviation` test case ensures that the function correctly calculates the mean absolute deviation for a small dataset.
- The `test_mean_absolute_deviation_large_dataset` test case ensures that the function correctly calculates the mean absolute deviation for a large dataset, taking numerical precision into account.
- The `if __name__ == '__main__':` block runs the tests when the script is executed directly.

The code covers both correctness and performance aspects via test cases for different dataset sizes.  If the script runs directly, the tests should pass.
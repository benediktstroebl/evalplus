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
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)
        self.assertEqual(mean_absolute_deviation([0., 0., 0.]), 0.0)
    def test_mean_absolute_deviation_large_dataset(self):
        self.assertAlmostEqual(mean_absolute_deviation([1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]), 2.5)
if __name__ == '__main__':
    unittest.main()
```

This code uses the `numpy` library to provide an efficient implementation of calculating the mean absolute deviation. The `test_mean_absolute_deviation` tests check that the function returns 1.0 when the input list contains only the value 1.0, and returns 0.0 when the input list contains three identical zeros. The `test_mean_absolute_deviation_large_dataset` test verifies the behavior for a larger list of numbers. Finally, `unittest.main()` executes the test cases when this script is run directly.
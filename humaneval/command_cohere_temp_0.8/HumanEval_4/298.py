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
    def test_no_deviation(self):
        self.assertEqual(mean_absolute_deviation([1., 1., 1., 1.]), 0.)
    def test_negative_values(self):
        self.assertEqual(mean_absolute_deviation([1., -1., 1., -1.]), 2.)

if __name__ == '__main__':
    unittest.main()
```
This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It leverages the `numpy` library to operate on arrays, making the computation more efficient and concise. The function returns the mean absolute deviation of the input list. 

The script also includes a test class `TestMeanAbsoluteDeviation` that verifies the correctness of the function against basic and edge-case scenarios. 

The `unittest.main()` function is called to execute the tests.  This is executed when the script is run directly.
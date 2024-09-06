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
    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), None)

if __name__ == '__main__':
    unittest.main()
```
This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. 

The `TestMeanAbsoluteDeviation` class runs two test cases, one for an input list of four numbers where the mean absolute deviation should be 1.0, and one for a list of three zeros where the mean absolute deviation should be 0. 

The `if __name__ == '__main__':` block runs the tests when the script is run directly.

And finally, the function utilizes the `numpy` library to compute the mean absolute deviation, making use of vectorized operations to enhance performance and readability.
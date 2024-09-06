Here is a Python script with a self-contained function that solves the problem of calculating the mean absolute deviation of a list of numbers and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

The function `mean_absolute_deviation` calculates the mean absolute deviation of a list of numbers. It first calculates the mean of the numbers and then uses NumPy to compute the absolute deviations from the mean, returning the average of these deviations as the final answer.

To test this function, you can create a test list of numbers and assert that the answer matches the expected value. Here is an example:
```python
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        numbers = [1., 2., 3., 4.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0) 

if __name__ == '__main__':
    unittest.main()
```

This code creates a test list of numbers and compares the calculated mean absolute deviation to the expected value of 1.0. 

Finally, the `if __name__ == '__main__':` block runs the tests when the script is run directly.
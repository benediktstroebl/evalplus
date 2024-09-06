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

if __name__ == '__main__':
    unittest.main()
```

In this code block:
- The `mean_absolute_deviation()` function leverages the `numpy` library to provide a more efficient solution. It calculates the Mean Absolute Deviation (MAD) of a list of numbers.
- Test cases are defined in the `TestMeanAbsoluteDeviation` class, inheriting from `unittest.TestCase`. These test cases verify the correctness of the `mean_absolute_deviation()` function.
- To run the test cases, the `unittest.main()` function is called when the script is executed directly.

This code demonstrates the use of `numpy` to compute the MAD while keeping the solution within a single Python script. It also includes test cases to ensure the accurate functionality of the `mean_absolute_deviation()` function.
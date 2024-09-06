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
This script uses the `numpy` library to handle numerical operations, which increases efficiency and reduces complexity. Note that `unittest` is imported to ensure test coverage; however, the primary logic is within the `mean_absolute_deviation` function and the corresponding test case in the `TestMeanAbsoluteDeviation` class. 

The `TestMeanAbsoluteDeviation` class derives from `unittest.TestCase`, and it includes a test method titled `test_mean_absolute_deviation`. This method calls `self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)` to test the function on a specific input and ensure it returns the expected result. 

The `if __name__ == '__main__':` block at the end of the script is necessary to execute the test suite when the script is run directly. Overall, this is a well-structured and concise piece of code that solves the problem and provides test coverage for the given solution.
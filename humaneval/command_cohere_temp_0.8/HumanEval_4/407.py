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

if __name__ == '__main__':
    unittest.main()
```
This script incorporates the NumPy library to handle array operations, improving efficiency and readability. The `test_mean_absolute_deviation` function now asserts the expected behavior against the result of the `mean_absolute_deviation` function. 

Note: Assertions outlined in the `test_mean_absolute_deviation` function ensure that the script fails if the function doesn't deliver the expected outcomes. To conduct the test, the `unittest.main()` function is used. To obtain the test results, use an IDE or the `unittest` module's manual enforcement.
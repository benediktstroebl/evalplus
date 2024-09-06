Here is a Python script with a self-contained function that solves the problem of calculating the mean absolute deviation of a list of numbers and passes corresponding tests:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_with_list_of_numbers(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)

if __name__ == '__main__':
    unittest.main()
```

In the above code, the numpy library is used to calculate the mean and the absolute deviations with a single and faster `np.array()` line, and the `np.mean()` method is used to calculate the mean of the absolute deviations. The `unittest` module is used to define a test case that checks the result of the function for a sample list of numbers.
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
    def test_mean_absolute_deviation_with_negative_values(self):
        self.assertEqual(mean_absolute_deviation([1., -2., 3., -4.]), 2.0)

if __name__ == '__main__':
    unittest.main()
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It utilizes the `numpy` library to operate on arrays and perform calculations efficiently. The function takes a list of numbers as input and returns the mean absolute deviation as a float.

The script also includes a unit test class `TestMeanAbsoluteDeviation` that verifies the correctness of the `mean_absolute_deviation` function. It contains two test methods: `test_mean_absolute_deviation` checks the function's result for two lists of numbers, and `test_mean_absolute_deviation_with_negative_values` verifies the function's behavior with a list that includes negative values.

To run the script, execute `python test_mean_absolute_deviation.py` in your terminal. The `unittest` framework will run the test methods, and thereafter show the results, providing confidence in the functionality's correctness.
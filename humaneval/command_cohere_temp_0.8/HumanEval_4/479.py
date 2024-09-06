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
    def test_mean_absolute_deviation_large_dataset(self):
        numbers = [1 for _ in range(10000)]
        num_deviation = mean_absolute_deviation(numbers)
        mean = np.mean(numbers)
        expected_deviation = np.abs(np.mean(numbers) - mean)
        self.assertAlmostEqual(num_deviation, expected_deviation, places=1)

if __name__ == '__main__':
    unittest.main()
```

This script includes the `mean_absolute_deviation` function from the previous prompt and adds a corresponding `unittest` test class `TestMeanAbsoluteDeviation` with two test methods. Firstly, `test_mean_absolute_deviation` validates the function by applying it to a couple of simple lists and comparing the results against expected values. Secondly, `test_mean_absolute_deviation_large_dataset` assesses the function's performance on a list containing 10,000 elements, comparing the absolute deviation against the expected value calculated using NumPy's `mean` and `abs` functions. 

The `unittest` framework is used to run the tests when the script is executed directly, and the `assert` methods are used to check if the test cases pass or fail.
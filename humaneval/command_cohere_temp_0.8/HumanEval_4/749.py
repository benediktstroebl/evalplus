Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_basic(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)
    def test_mean_absolute_deviation_with_negative_values(self):
        self.assertEqual(mean_absolute_deviation([1., -2., 3., -4.]), 2.0)
    def test_mean_absolute_deviation_with_single_value(self):
        self.assertEqual(mean_absolute_deviation([10.0]), 0.0)
    def test_mean_absolute_deviation_with_empty_list(self):
        with self.assertRaises(ValueError):
            mean_absolute_deviation([])

if __name__ == '__main__':
    unittest.main()
```

This script includes the `mean_absolute_deviation` function, which calculates the mean absolute deviation of a list of numbers, and a set of unit tests, defined in the `TestMeanAbsoluteDeviation` class, that verify the function's behavior for various input scenarios.

The `mean_absolute_deviation` function leverages `numpy` to compute the absolute deviations and mean using `np.abs()` and `np.mean()` respectively, which leads to a more efficient and concise solution. 

The tests included in the `TestMeanAbsoluteDeviation` class cover various cases such as basic input, input with negative values, a single value, and an empty list. 

To run the tests, you can use the `unittest` module by calling `unittest.main()` at the end of the script, this will execute the tests and display the results. 

To run the script, save it as a `.py` file and execute it using a Python interpreter in your environment. 

You can also modify the script to include additional tests to further validate the `mean_absolute_deviation` function. 

Let me know if you need any further modifications or if you want to go through any other coding problems!
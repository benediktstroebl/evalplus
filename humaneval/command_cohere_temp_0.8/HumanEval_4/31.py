Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_basic(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.)

    def test_mean_absolute_deviation_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.)

    def test_mean_absolute_deviation_negative_values(self):
        self.assertEqual(mean_absolute_deviation([1., -2., 3., -4.]), 2.) 

if __name__ == '__main__':
    unittest.main()
```
This script includes the `mean_absolute_deviation` function and a set of unit tests defined in `TestMeanAbsoluteDeviation`. 
The function calculates the mean absolute deviation of a list of numbers using the `numpy` library. 

The center of the calculation is the mean value, and the variability is measured as the absolute deviation from the center. The unit tests check the functionality of the `mean_absolute_deviation` function with three different scenarios. 

The first test checks the function with a basic example. The second test checks the function with an empty list, and the third test checks the function with negative values. 

When you run the script, the unit tests are automatically executed, ensuring that the function behaves as expected.  This approach helps to keep the code maintainable and helps to detect errors that might occur in the future because of changes in the code base.
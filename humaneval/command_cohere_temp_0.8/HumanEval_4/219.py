Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)
    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.)
    def test_large_deviations(self):
        self.assertAlmostEqual(mean_absolute_deviation([5., 50., 100., 150.]), 17.5)

if __name__ == '__main__':
    unittest.main()
```
This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It utilizes the `numpy` library to perform the necessary calculations. 

The function takes a list of numbers as input and returns the mean absolute deviation of the list. The function calculates the mean of the absolute differences between each element in the list and the mean of the list. 

It uses the `unittest` module to perform tests on the `mean_absolute_deviation` function. The `TestMeanAbsoluteDeviation` class includes three test methods. `test_basic` verifies the function's success on a simple list, `test_empty_list` checks that the function handles an empty list properly, and `test_large_deviations` examines the function's behavior on a list with larger deviations. 

Finally, the `if __name__ == '__main__':` block runs the tests when the script is executed directly. 

Note: This solution relies on the `numpy` library, which you'll need to install separately if you haven't already. You can install it using `pip`: `pip install numpy`.
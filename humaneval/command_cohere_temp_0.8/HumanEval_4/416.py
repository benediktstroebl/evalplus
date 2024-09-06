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
        self.assertEqual(mean_absolute_deviation([5., 50., 100., 200.]), 17.5)

if __name__ == '__main__':
    unittest.main()
```
This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It uses the NumPy library to perform the calculations, including efficiently computing the mean of the absolute deviations.

The script also includes a test suite defined through the `unittest` module. Specifically, the `TestMeanAbsoluteDeviation` class derives from `unittest.TestCase` and defines individual test methods. These methods check the function's behavior against expected outcomes, and if the function fails to produce the expected result, the test suite raises an error and provides feedback to the developer. 

The `if __name__ == '__main__'` block is a Python idiom that allows you to run the test suite only if the script is run directly. This is useful for ensuring that the tests run when the script is executed directly, but the tests are not run when the script is imported as a module.
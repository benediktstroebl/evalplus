Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_with_list_of_numbers(self):
        numbers = [1., 2., 3., 4.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

    def test_mean_absolute_deviation_with_list_of_strings(self):
        self.assertRaises(TypeError, mean_absolute_deviation, ["apple", "banana", "cherry"])

if __name__ == '__main__':
    unittest.main()
```

In the above code, the numpy library has been imported and the `mean_absolute_deviation()` function accepts a list of numbers, uses numpy to compute the mean and absolute deviations, and then returns the Mean Absolute Deviation. The `TestMeanAbsoluteDeviation` class inherits from `unittest.TestCase` and has two test methods. 

The first test method verifies the function against a list of numbers, ensuring the calculated Mean Absolute Deviation matches the expected value. The second test method checks if the function raises a `TypeError` when given a list of strings, confirming the function's expectation of a numeric list input. 

The `if __name__ == '__main__':` line facilitates the running of tests when the script is executed directly. 

This code will provide a valid testing framework to validate the `mean_absolute_deviation()` function.
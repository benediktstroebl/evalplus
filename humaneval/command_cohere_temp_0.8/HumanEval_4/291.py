Here's a Python script with a self-contained function that solves the problem you've outlined, along with a separate test module to validate its correctness:
```python
# problem_solving.py

from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    if not numbers:
        raise ValueError("Input list is empty. Cannot calculate Mean Absolute Deviation.")
    
    mean = sum(numbers) / len(numbers)
    devations = [abs(num - mean) for num in numbers]
    return sum(devations) / len(numbers)

# Tests
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_empty_list(self):
        self.assertRaises(ValueError, mean_absolute_deviation, [])
    
    def test_single_value(self):
        self.assertEqual(mean_absolute_deviation([5.0]), 0.0)
    
    def test_symmetric_distribution(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)
    
    def test_asymmetric_distribution(self):
        self.assertAlmostEqual(mean_absolute_deviation([2.0, 5.0, 3.0, 7.0, 4.0]), 3.0, places=2)

if __name__ == '__main__':
    unittest.main()
```

The `mean_absolute_deviation` function is designed to calculate the Mean Absolute Deviation (MAD) of a list of numbers. It begins by checking if the input list is empty, raising a `ValueError` if empty. It then calculates the mean of the numbers and computes the absolute differences between each number and the mean, averaging these differences to return the MAD. 

The `TestMeanAbsoluteDeviation` class inherits from `unittest.TestCase` and contains several test methods. `test_empty_list` checks if the function raises a `ValueError` when an empty list is passed in. `test_single_value` and `test_symmetric_distribution` verify that the function returns 0.0 and 1.0, respectively, for lists containing a single value or a symmetrically distributed set of numbers. Finally, `test_asymmetric_distribution` checks the function's handling of an asymmetric distribution. 

By running `unittest.main()` at the end of the script, the test cases are automatically executed when the script is run directly. 

This code provides a clear and concise way to solve the provided problem, while also ensuring the functionality is correctly validated through the test suite. Let me know if you have any questions or if you'd like me to explain any part of the solution in more detail!
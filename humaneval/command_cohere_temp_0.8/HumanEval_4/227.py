Here's a Python script with a self-contained function that solves the problem you've outlined, along with a separate test module to validate its correctness:
```python
# problem_solver.py
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
   Returns:
    (float): Mean Absolute Deviation of the input list of numbers.
    """
    if not numbers:
        raise ValueError("Input list 'numbers' cannot be empty.")
    
    mean = sum(numbers) / len(numbers)
    deviations = [abs(x - mean) for x in numbers]
    return sum(deviations) / len(numbers)

# Tests
import unittest

def test_mad() -> None:
    """ Unit tests for mean_absolute_deviation function. """
    
    # Test cases with equal values
    self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.)
    self.assertEqual(mean_absolute_deviation([0., 0., 0., 0.]), 0.)
    self.assertEqual(mean_absolute_deviation([10., 10., 10., 10.]), 0.)
    
    # Test case with positive and negative values
    self.assertAlmostEqual(mean_absolute_deviation([1., 2., -3., 4.]), 1.5)
    
    # Edge case: Empty list
    self.assertRaises(ValueError, mean_absolute_deviation, [])

if __name__ == '__main__':
    unittest.main()
```

In this script, the `mean_absolute_deviation` function calculates the mean absolute deviation of a list of numbers. It first checks if the input list is empty, raising a `ValueError` if so. It then calculates the mean of the numbers and creates a list of absolute deviations from the mean for each number. Finally, it returns the average of these deviations.
Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    if not numbers:
        raise ValueError("Input list is empty. Cannot compute MAD.")

    mean = math.mean(numbers)
    deviations = [abs(num - mean) for num in numbers]
    return math.mean(deviations)
```

This script includes the `mean_absolute_deviation` function that takes a list of numbers as input and returns the mean absolute deviation of the list. It first checks if the input list is empty and raises a `ValueError` if so. It then calculates the mean of the numbers in the list and creates a list of absolute deviations from the mean for each number. It then calculates the mean of these absolute deviations and returns it as the mean absolute deviation of the list. 

To verify the correctness of this function, you can use the following tests:
```python
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_empty_input(self):
        self.assertRaises(ValueError, mean_absolute_deviation, [])

    def test_single_number(self):
        self.assertEqual(mean_absolute_deviation([10.0]), 0.0)

    def test_symmetric_distribution(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

    def test_asymmetric_distribution(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        expected_mad = sum([abs(num - (sum(numbers) / len(numbers))) for num in numbers]) / len(numbers)
        self.assertEqual(mean_absolute_deviation(numbers), expected_mad)

if __name__ == '__main__':
    unittest.main()
```

These tests aim to cover different scenarios, including an empty input list, a list with a single number, a symmetrically distributed list, and an asymmetrically distributed list.
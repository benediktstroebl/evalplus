```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
        numbers (List[float]): A list of input numbers.
    
    Returns:
        float: The Mean Absolute Deviation of the input numbers.
    """
    
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each number and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0


# Test cases
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    
    def test_mad(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)
        self.assertAlmostEqual(mean_absolute_deviation([5.0, 5.0, 5.0, 5.0]), 0.0)
        self.assertAlmostEqual(mean_absolute_deviation([10.0, 20.0, 30.0, 40.0]), 15.0)

if __name__ == '__main__':
    unittest.main()
```
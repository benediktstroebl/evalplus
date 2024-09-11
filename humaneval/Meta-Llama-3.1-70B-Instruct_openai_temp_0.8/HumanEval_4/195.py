```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a dataset.

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    float: The Mean Absolute Deviation.
    """
    # Calculate the mean of the dataset
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_differences = [abs(num - mean) for num in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_differences) / len(absolute_differences)
    
    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0


# Test cases
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_example_usage(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)
    
    def test_single_element(self):
        self.assertEqual(mean_absolute_deviation([5.0]), 0.0)
    
    def test_identical_elements(self):
        self.assertEqual(mean_absolute_deviation([2.0, 2.0, 2.0, 2.0]), 0.0)

if __name__ == '__main__':
    unittest.main()
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. It first calculates the mean of the dataset, then calculates the absolute difference between each element and the mean, and finally calculates the Mean Absolute Deviation by averaging these absolute differences.

The script also includes example usage and test cases using the `unittest` framework to verify the correctness of the `mean_absolute_deviation` function.
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
        numbers: A list of float numbers.
    
    Returns:
        A float number representing the Mean Absolute Deviation.
    """
    
    # First, calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Then, calculate the absolute difference between each number and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Finally, calculate the mean of these absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
This script calculates the Mean Absolute Deviation (MAD) of a list of numbers around their mean. The MAD is a measure of the average distance between each data point and the mean of the dataset. It is a useful metric for understanding the spread of a dataset.
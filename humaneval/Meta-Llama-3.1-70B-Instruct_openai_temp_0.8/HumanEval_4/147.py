```python
from typing import List

def calculate_mean(numbers: List[float]) -> float:
    """
    Calculate the mean of a list of numbers.
    
    Args:
    numbers (List[float]): A list of float numbers.
    
    Returns:
    float: The mean of the input numbers.
    """
    return sum(numbers) / len(numbers)


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
    numbers (List[float]): A list of float numbers.
    
    Returns:
    float: The mean absolute deviation of the input numbers.
    """
    # Calculate the mean of the input numbers
    mean = calculate_mean(numbers)
    
    # Calculate the absolute difference between each number and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = calculate_mean(absolute_diffs)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(mad)  # Output: 1.0
```
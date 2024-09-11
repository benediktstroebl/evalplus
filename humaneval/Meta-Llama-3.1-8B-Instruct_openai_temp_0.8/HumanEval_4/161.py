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
    numbers (List[float]): A list of floating point numbers.
    
    Returns:
    float: The mean absolute deviation of the input list.
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute differences between each element and the mean
    absolute_differences = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences (Mean Absolute Deviation)
    mad = sum(absolute_differences) / len(absolute_differences)
    
    return mad

# Example usage:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
print(mean_absolute_deviation([5.0, 5.0, 5.0]))  # Output: 0.0
```

This script defines a function `mean_absolute_deviation` that calculates the mean absolute deviation of a given list of numbers. It first calculates the mean of the input list, then the absolute differences between each element and the mean, and finally the mean of these absolute differences. The function raises a `ValueError` if the input list is empty. The example usage shows how to use this function with different input lists.
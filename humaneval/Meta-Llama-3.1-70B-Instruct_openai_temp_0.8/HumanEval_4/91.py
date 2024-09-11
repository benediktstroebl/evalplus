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
        float: The Mean Absolute Deviation of the input list.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list is empty")
    
    # Calculate the mean of the input list
    mean_value = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_differences = [abs(x - mean_value) for x in numbers]
    
    # Calculate the mean of the absolute differences
    mad = sum(absolute_differences) / len(absolute_differences)
    
    return mad


# Example usage:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```

This script calculates the Mean Absolute Deviation (MAD) of a given list of numbers. It first calculates the mean of the input list, then calculates the absolute difference between each element and the mean. Finally, it calculates the mean of these absolute differences to get the MAD. If the input list is empty, it raises a ValueError.
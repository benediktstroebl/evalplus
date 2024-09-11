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
        numbers (List[float]): A list of float numbers

    Returns:
        float: The Mean Absolute Deviation of the input list

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Calculate the mean of the numbers list
    mean = sum(numbers) / len(numbers)
    
    # Initialize a variable to hold the sum of absolute differences
    absolute_diff_sum = 0
    
    # Iterate through each number in the list
    for num in numbers:
        # Calculate the absolute difference between the number and the mean
        absolute_diff = abs(num - mean)
        
        # Add the absolute difference to the sum
        absolute_diff_sum += absolute_diff
    
    # Calculate the mean absolute deviation
    mad = absolute_diff_sum / len(numbers)
    
    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. It first calculates the mean of the list, then the sum of absolute differences between each number and the mean, and finally returns the mean of these absolute differences. The script includes docstrings that explain the purpose and usage of the function, as well as an example use case.
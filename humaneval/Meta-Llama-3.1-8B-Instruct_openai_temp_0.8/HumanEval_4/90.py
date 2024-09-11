```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    Parameters:
    numbers (List[float]): list of numbers
    Returns:
    float: mean absolute deviation of the input list
    """
    
    # calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # calculate the absolute difference between each number and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script uses a list comprehension to calculate the absolute deviations from the mean, and then calculates the mean of these deviations to find the Mean Absolute Deviation.
```python
from typing import List
import statistics

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
        float: Mean Absolute Deviation.
    """
    # Check if the list is empty
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the mean
    mean_value = statistics.mean(numbers)
    
    # Calculate the absolute deviation from the mean for each number
    absolute_deviations = [abs(num - mean_value) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This code uses the `statistics` module, which is part of Python's standard library. It calculates the mean absolute deviation by first calculating the mean of the input numbers, then calculating the absolute deviation from the mean for each number, and finally calculating the mean of these absolute deviations.
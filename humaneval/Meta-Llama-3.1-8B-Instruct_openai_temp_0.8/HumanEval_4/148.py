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
    float: The mean absolute deviation of the input list.
    """
    # Check if the list is empty
    if not numbers:
        raise ValueError("Input list is empty")
    
    # Calculate the mean of the input list
    mean = statistics.mean(numbers)
    
    # Calculate the mean absolute deviation
    mad = statistics.median([abs(x - mean) for x in numbers])
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script uses the `statistics` library to calculate the mean and median of the input list. The `mean_absolute_deviation` function takes a list of numbers, calculates the mean of this list, and then calculates the median of the absolute differences between each number and the mean. The result is the mean absolute deviation of the input list. 

Please note that the median is used instead of the mean in the calculation of the mean absolute deviation to avoid bias due to outliers.
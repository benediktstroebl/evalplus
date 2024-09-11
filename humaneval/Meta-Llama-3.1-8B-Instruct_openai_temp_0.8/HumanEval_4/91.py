```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ Calculate Mean Absolute Deviation around the mean of a dataset.
    
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
        numbers (List[float]): A list of input numbers.
    
    Returns:
        float: Mean Absolute Deviation.
    
    Examples:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    
    # Calculate the mean of the given numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviation from the mean for each number
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers. It uses the `statistics` module to calculate the mean of the numbers and the absolute deviations from the mean. The MAD is then calculated as the average of these absolute deviations. The example usage shows how to use this function with a list of numbers.
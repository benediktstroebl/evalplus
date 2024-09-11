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

    Parameters:
    numbers (List[float]): A list of float numbers.

    Returns:
    float: Mean Absolute Deviation of the given list of numbers.

    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Calculate the mean of the numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviations from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean absolute deviation using the statistics module
    mad = statistics.mean(absolute_deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a list of numbers. It uses the `statistics` module to calculate the mean of the numbers and the absolute deviations from the mean. The example usage at the end demonstrates how to use the function with a list of numbers.
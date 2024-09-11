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
    numbers (List[float]): A list of input numbers.

    Returns:
    float: The Mean Absolute Deviation of the input list.

    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Calculate the mean of the input numbers
    mean = statistics.mean(numbers)
    
    # Use a list comprehension to calculate the absolute difference between each number and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad


# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script uses the built-in `statistics` module to calculate the mean of the input numbers. It then calculates the absolute difference between each number and the mean using a list comprehension. Finally, it calculates the mean of these absolute deviations to get the Mean Absolute Deviation.
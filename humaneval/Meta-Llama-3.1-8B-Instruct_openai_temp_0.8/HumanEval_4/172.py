### Mean Absolute Deviation Calculator
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
        numbers: A list of floating point numbers

    Returns:
        The Mean Absolute Deviation of the input list

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Calculate the mean of the input list
    mean = statistics.mean(numbers)
    
    # Calculate the absolute difference between each element and the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = statistics.mean(deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script uses the `statistics` module to calculate the mean of the input list, and then calculates the Mean Absolute Deviation by taking the mean of the absolute differences between each element and the mean. The result is printed to the console. 

Note: This script assumes that the input list is non-empty. If the input list is empty, it will raise a `StatisticsError`. If you need to handle empty lists, you should add error checking code to handle this case.
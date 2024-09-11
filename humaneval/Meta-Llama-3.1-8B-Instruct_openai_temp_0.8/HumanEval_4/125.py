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
    float: The Mean Absolute Deviation of the input list.
    """
    
    # Calculate the mean of the numbers
    mean_value = statistics.mean(numbers)
    
    # Calculate the absolute deviation of each number from the mean
    deviations = [abs(num - mean_value) for num in numbers]
    
    # Calculate the mean of the deviations
    mad = statistics.mean(deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script uses Python's built-in `statistics` module to efficiently calculate the mean of the input numbers and the mean of the absolute deviations. The absolute deviations are calculated using a list comprehension. The result is then returned as the Mean Absolute Deviation.
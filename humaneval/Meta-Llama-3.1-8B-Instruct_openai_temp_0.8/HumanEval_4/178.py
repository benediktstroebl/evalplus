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

    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Calculate the mean of the dataset
    mean = statistics.mean(numbers)

    # Calculate the absolute differences between each number and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)

    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print("Mean Absolute Deviation:", result)
```

This script uses the `statistics` module to calculate the mean of the input list. It then calculates the absolute differences between each number and the mean, and finally calculates the mean of these absolute deviations to find the Mean Absolute Deviation.
### Mean Absolute Deviation Calculator
#### A Python Script to Calculate the Mean Absolute Deviation

```python
from typing import List
import statistics  # Import the statistics module for mean calculation

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
        float: The mean absolute deviation of the input numbers.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    mean = statistics.mean(numbers)  # Calculate the mean of the input list
    absolute_deviations = [abs(num - mean) for num in numbers]  # Calculate the absolute deviations
    mad = statistics.mean(absolute_deviations)  # Calculate the mean of the absolute deviations
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation: {result}")
```

In this script, we utilize the `statistics` module to calculate the mean of the input numbers, which simplifies the process and ensures accuracy. We then calculate the absolute deviations from the mean, and finally, we calculate the mean of these absolute deviations, which is the Mean Absolute Deviation.
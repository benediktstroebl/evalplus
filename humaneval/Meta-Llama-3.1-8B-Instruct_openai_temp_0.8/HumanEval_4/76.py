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
        numbers (List[float]): A list of input numbers

    Returns:
        float: Mean Absolute Deviation of the input list

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input list
    mean = statistics.mean(numbers)

    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = [abs(x - mean) for x in numbers]

    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)

    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
print(mean_absolute_deviation([2.0, 4.0, 6.0, 8.0]))  # Output: 2.0
print(mean_absolute_deviation([10.0, 20.0, 30.0, 40.0]))  # Output: 10.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. The function uses the `statistics` module to calculate the mean of the input list and the absolute deviations of each number from the mean. The mean of the absolute deviations is then calculated and returned. The script includes a test at the end to demonstrate the function's usage.
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
        numbers (List[float]): A list of numbers.

    Returns:
        float: The Mean Absolute Deviation of the input numbers.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """

    # Check if the input list is not empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the numbers
    mean = statistics.mean(numbers)

    # Calculate the absolute difference between each number and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_diffs)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers. It uses the `statistics` module to calculate the mean and the `abs` function to calculate the absolute differences. The function also includes input validation to check if the input list is not empty. The example usage at the end shows how to use the function with a sample list of numbers.
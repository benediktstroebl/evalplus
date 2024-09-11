```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
        numbers (List[float]): A list of numerical values.

    Returns:
        float: The Mean Absolute Deviation of the input list.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviation of each number from the mean
    deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = sum(deviations) / len(deviations)

    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation of the input list. It calculates the mean of the input list, then calculates the absolute deviation of each number from the mean, and finally calculates the mean of these absolute deviations. The script also includes a test case to demonstrate the function's usage.
### Mean Absolute Deviation Calculator

Below is a Python script that defines a function to calculate the Mean Absolute Deviation (MAD) of a given list of numbers.

```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
        numbers (List[float]): A list of input numbers.

    Returns:
        float: The Mean Absolute Deviation.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Check if the input list is empty
    if len(numbers) == 0:
        return None

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviations from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_deviations) / len(absolute_deviations)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input, calculates the mean of the list, computes the absolute deviations from the mean, and returns the Mean Absolute Deviation. The function also includes a check for an empty input list and provides an example usage at the end.
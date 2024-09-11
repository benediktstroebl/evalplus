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
        numbers (List[float]): A list of floating point numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Initialize a variable to store the absolute deviations
    absolute_deviations = 0

    # Iterate over the input list to calculate the absolute deviations
    for num in numbers:
        absolute_deviations += abs(num - mean)

    # Calculate the Mean Absolute Deviation
    mad = absolute_deviations / len(numbers)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script defines the `mean_absolute_deviation` function to calculate the Mean Absolute Deviation of a given list of numbers. It first calculates the mean of the input list, then iterates over the list to calculate the absolute deviations from the mean. Finally, it calculates the Mean Absolute Deviation by dividing the sum of absolute deviations by the length of the input list. The result is returned as a floating point number.
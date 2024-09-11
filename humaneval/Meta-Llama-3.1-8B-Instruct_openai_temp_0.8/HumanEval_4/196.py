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
        float: The mean absolute deviation of the input list.

    Examples:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviation from the mean for each number
    deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the deviations (Mean Absolute Deviation)
    mad = sum(deviations) / len(deviations)

    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This Python script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a list of numbers. It first calculates the mean of the input list, then the absolute deviation from the mean for each number, and finally the mean of these deviations, which is the Mean Absolute Deviation. The function is tested with a sample list of numbers.
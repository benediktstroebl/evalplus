```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) of a given list of numbers.

    MAD is the average absolute difference between each element and the mean of the dataset.

    Args:
        numbers: A list of floating-point numbers.

    Returns:
        The Mean Absolute Deviation of the input numbers.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Calculate the mean of the input numbers
    mean = statistics.mean(numbers)

    # Calculate the absolute difference between each number and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation: {mad}")
```

This script defines a function `mean_absolute_deviation` that takes a list of floating-point numbers as input and returns the Mean Absolute Deviation (MAD) of the input numbers. The MAD is calculated by first finding the mean of the input numbers, then calculating the absolute difference between each number and the mean, and finally finding the mean of these absolute deviations. The script also includes an example usage of the function.
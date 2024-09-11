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
        numbers (List[float]): A list of numbers.

    Returns:
        float: The mean absolute deviation of the input numbers.
    """
    if not numbers:
        raise ValueError("Input list must be non-empty")

    mean = sum(numbers) / len(numbers)
    absolute_deviations = [abs(num - mean) for num in numbers]
    mad = sum(absolute_deviations) / len(absolute_deviations)
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This Python script defines a function `mean_absolute_deviation` that takes a list of float numbers as input and returns their Mean Absolute Deviation (MAD). It first calculates the mean of the input numbers, then computes the absolute deviations of each number from the mean, and finally returns the average of these absolute deviations. The script also includes example usage to demonstrate how to call the function.
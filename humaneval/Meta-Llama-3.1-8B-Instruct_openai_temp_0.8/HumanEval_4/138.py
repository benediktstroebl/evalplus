Here's a Python script that implements the `mean_absolute_deviation` function as described:
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
    numbers (List[float]): A list of floating-point numbers.

    Returns:
    float: The mean absolute deviation of the input numbers.

    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviation from the mean for each number
    absolute_deviations = [abs(x - mean) for x in numbers]

    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
This script defines the `mean_absolute_deviation` function, which takes a list of floating-point numbers as input and returns the mean absolute deviation of these numbers. It first checks if the input list is empty, and raises a `ValueError` if it is. It then calculates the mean of the input numbers, and the absolute deviation from the mean for each number. Finally, it calculates the mean of these absolute deviations, which is the mean absolute deviation of the input numbers. The script also includes an example usage of the function.
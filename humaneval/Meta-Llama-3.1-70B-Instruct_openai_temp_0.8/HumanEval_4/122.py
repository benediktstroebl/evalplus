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
    float: The Mean Absolute Deviation of the given list of numbers.

    Raises:
    ValueError: If the input list is empty.
    """

    # Check if the list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the given list of numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each number and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]

    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_diffs) / len(absolute_diffs)

    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers. It first checks if the input list is empty and raises a `ValueError` if it is. Then it calculates the mean of the numbers, computes the absolute difference between each number and the mean, and finally calculates the MAD by averaging these absolute differences. The function includes a docstring that explains its purpose, parameters, return value, and any raised exceptions. The example usage demonstrates how to use the function with a sample list of numbers.
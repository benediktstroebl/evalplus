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
        numbers: A list of numbers.

    Returns:
        Mean Absolute Deviation of the input numbers.

    Raises:
        ValueError: If the input list is empty.
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the input numbers
    mean_value = sum(numbers) / len(numbers)

    # Calculate the absolute deviations from the mean
    absolute_deviations = [abs(num - mean_value) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad_value = sum(absolute_deviations) / len(absolute_deviations)

    return mad_value


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation of {numbers}: {mad}")
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation (MAD) of the input numbers. The MAD is calculated by first finding the mean of the input numbers, then calculating the absolute deviations of each number from the mean, and finally finding the mean of these absolute deviations.

The script also includes a check for an empty input list and raises a `ValueError` in this case.

The example usage at the end demonstrates how to use the `mean_absolute_deviation` function with a sample list of numbers and print the result.
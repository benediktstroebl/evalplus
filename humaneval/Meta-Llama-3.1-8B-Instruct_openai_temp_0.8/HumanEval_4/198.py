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
        numbers (List[float]): A list of floating point numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    # Check if the list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the list
    mean = statistics.mean(numbers)

    # Calculate the absolute deviations from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the Mean Absolute Deviation
    mad = statistics.mean(absolute_deviations)

    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a list of numbers. It uses the `statistics` module to calculate the mean of the list and then calculates the absolute deviations from the mean. Finally, it calculates the MAD by taking the mean of these absolute deviations. The function raises a `ValueError` if the input list is empty. The example usage demonstrates how to use this function with a list of numbers.
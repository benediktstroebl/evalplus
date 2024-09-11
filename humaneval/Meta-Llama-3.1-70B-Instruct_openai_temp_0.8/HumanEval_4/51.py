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
        float: The Mean Absolute Deviation of the input numbers.
    """

    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviations from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)

    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script calculates the Mean Absolute Deviation (MAD) of a given list of numbers. The MAD is the average absolute difference between each element and the mean of the dataset. The script first calculates the mean of the numbers, then calculates the absolute deviations from the mean, and finally calculates the mean of these absolute deviations. If the input list is empty, the script raises a ValueError. The example usage demonstrates how to use the `mean_absolute_deviation` function with a list of numbers.
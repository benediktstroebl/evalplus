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
    """
    # Check if the list is empty
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute differences between each number and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that takes a list of floating point numbers and returns the Mean Absolute Deviation (MAD) of the input list. The MAD is calculated by first finding the mean of the input list, then calculating the absolute differences between each number and the mean, and finally averaging these differences. The function raises a `ValueError` if the input list is empty. The example usage at the end demonstrates how to use this function with a list of numbers.
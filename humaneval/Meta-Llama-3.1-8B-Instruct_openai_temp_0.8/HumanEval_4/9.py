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
    numbers (List[float]): A list of numbers

    Returns:
    float: The Mean Absolute Deviation
    """
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]

    # Calculate the Mean Absolute Deviation
    mad = sum(deviations) / len(deviations)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. It first calculates the mean of the numbers, then calculates the absolute deviations from the mean, and finally calculates the Mean Absolute Deviation by taking the average of the absolute deviations. The example usage demonstrates how to use the function with a list of numbers.
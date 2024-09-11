### Mean Absolute Deviation Calculation
#### Calculation Script
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
    numbers (List[float]): A list of numbers to calculate MAD from

    Returns:
    float: The Mean Absolute Deviation of the input list
    """
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute differences between each element and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)

    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation of the list. The function first calculates the mean of the input list, then calculates the absolute differences between each element and the mean, and finally calculates the mean of these absolute deviations.
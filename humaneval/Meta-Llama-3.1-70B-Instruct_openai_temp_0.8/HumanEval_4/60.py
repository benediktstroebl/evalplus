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
        numbers: A list of float numbers.

    Returns:
        Mean Absolute Deviation of the input numbers.
    """
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad


# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that takes a list of float numbers as input, calculates the mean of the numbers, calculates the absolute deviation of each number from the mean, and finally returns the mean of the absolute deviations. The script also includes a test case at the end to demonstrate the usage of the function.
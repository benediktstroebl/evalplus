```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
        numbers (List[float]): A list of input numbers.

    Returns:
        float: The mean absolute deviation of the input numbers.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each number and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
print(mean_absolute_deviation([1.0, 3.0, 3.0, 7.0]))  # Output: 1.75
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input and returns their mean absolute deviation. It first calculates the mean of the input numbers, then calculates the absolute difference between each number and the mean, and finally calculates the mean of these absolute differences. The function is tested with two examples.
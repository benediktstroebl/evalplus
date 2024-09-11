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
    numbers (List[float]): A list of numbers.

    Returns:
    float: The Mean Absolute Deviation.

    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    mean = sum(numbers) / len(numbers)
    absolute_deviations = [abs(num - mean) for num in numbers]
    return sum(absolute_deviations) / len(absolute_deviations)


# Testing the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script calculates the Mean Absolute Deviation (MAD) for a given list of numbers. It first calculates the mean of the list, then it calculates the absolute difference between each number and the mean. Finally, it returns the average of these absolute differences, which is the Mean Absolute Deviation.
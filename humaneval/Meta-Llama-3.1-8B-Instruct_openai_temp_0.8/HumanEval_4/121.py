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
        numbers (List[float]): A list of float numbers.

    Returns:
        float: The mean absolute deviation of the input list.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each element and the mean
    abs_diff = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute differences
    mad = sum(abs_diff) / len(abs_diff)

    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers. It first calculates the mean of the list, then calculates the absolute difference between each number and the mean, and finally calculates the mean of these absolute differences. The function includes input validation to check if the input list is empty, and it raises a `ValueError` if it is.
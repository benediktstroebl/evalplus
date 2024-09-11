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
    float: Mean Absolute Deviation of the input numbers.

    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """

    # Check if the input list is empty
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty.")

    # Calculate the mean of the numbers
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

This Python script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. The function first calculates the mean of the input numbers, then calculates the absolute deviation of each number from the mean, and finally calculates the mean of these absolute deviations. The result is returned as a floating point number. If the input list is empty, a `ValueError` is raised. The script includes a test case to demonstrate the function's usage.
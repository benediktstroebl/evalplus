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
        float: The mean absolute deviation.
    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute differences from the mean
    absolute_differences = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute differences
    mad = sum(absolute_differences) / len(absolute_differences)

    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function first calculates the mean of the numbers, then calculates the absolute differences from the mean, and finally calculates the mean of the absolute differences. The result is returned as a float.

The script also includes a check to raise a `ValueError` if the input list is empty, and an example usage of the function with a list of numbers.
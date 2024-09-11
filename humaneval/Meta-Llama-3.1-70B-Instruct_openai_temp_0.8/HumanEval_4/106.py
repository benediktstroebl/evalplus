```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation around the mean of a given list of numbers.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    float: The Mean Absolute Deviation.

    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """

    # Check if input list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each number and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]

    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_diffs) / len(absolute_diffs)

    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(mad)  # Output: 1.0
```
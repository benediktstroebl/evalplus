```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation around the mean of the input dataset.

    Args:
        numbers (List[float]): A list of input numbers.

    Returns:
        float: The Mean Absolute Deviation.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input dataset
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(x - mean) for x in numbers]

    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_diffs) / len(numbers)

    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"The Mean Absolute Deviation is: {mad}")
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation around the mean of the input dataset. The function takes a list of numbers as input, calculates the mean, absolute differences between each element and the mean, and finally returns the Mean Absolute Deviation. The script also includes an example usage and a docstring with explanations and an example.
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a given dataset.

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    float: The Mean Absolute Deviation.

    Raises:
    ValueError: If the input list is empty.

    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """

    # Check if input list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute differences between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute differences (Mean Absolute Deviation)
    mad = sum(absolute_diffs) / len(absolute_diffs)

    return mad


# Example usage
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0]
    mad = mean_absolute_deviation(numbers)
    print(f"Mean Absolute Deviation: {mad}")
```

This script calculates the Mean Absolute Deviation of a given list of numbers by first calculating the mean, then the absolute differences between each element and the mean, and finally the mean of these absolute differences. It includes input validation, raises an error for empty input lists, and demonstrates example usage.
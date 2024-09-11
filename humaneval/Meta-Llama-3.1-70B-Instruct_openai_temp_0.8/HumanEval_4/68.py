```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a given dataset.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    float: The Mean Absolute Deviation of the input numbers.

    Raises:
    ValueError: If the input list is empty.
    """

    # Check for empty list
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)

    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This Python script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers. The function first calculates the mean of the numbers, then calculates the absolute deviation of each number from the mean, and finally calculates the mean of these absolute deviations. The result is the MAD of the input numbers. The script also includes example usage and error handling for an empty input list.
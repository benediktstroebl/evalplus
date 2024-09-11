```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a given dataset.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    float: The Mean Absolute Deviation of the input numbers.
    """
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(x - mean) for x in numbers]

    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)

    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines the `mean_absolute_deviation` function, which takes a list of floating point numbers as input, calculates the mean of the input numbers, computes the absolute difference between each element and the mean, and then calculates the mean of these absolute differences. The function includes a check to raise a `ValueError` if the input list is empty.

You can run the script and test the function with the provided example usage.
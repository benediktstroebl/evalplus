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
        numbers: A list of floating point numbers.
    
    Returns:
        The Mean Absolute Deviation of the input numbers.
    """

    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute differences from the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation: {mad}")
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a list of numbers. It first checks if the input list is empty, then calculates the mean of the numbers, the absolute differences from the mean, and finally the mean of these absolute differences. The result is returned as a float.

The example usage demonstrates how to use the function with a list of numbers and print the result.
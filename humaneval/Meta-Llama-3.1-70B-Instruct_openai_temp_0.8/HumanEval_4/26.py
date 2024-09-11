```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a dataset.

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    float: The Mean Absolute Deviation.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input numbers
    mean_value = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(x - mean_value) for x in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation: {result}")
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. It first calculates the mean of the input numbers, then calculates the absolute difference between each element and the mean, and finally returns the average of these absolute differences.

The example usage at the end of the script demonstrates how to use the function with the input `[1.0, 2.0, 3.0, 4.0]` and prints the result.
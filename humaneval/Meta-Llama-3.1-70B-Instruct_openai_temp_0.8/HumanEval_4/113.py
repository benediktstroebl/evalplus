```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a given dataset.

    Args:
    numbers: A list of float numbers.

    Returns:
    The Mean Absolute Deviation of the input dataset.

    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Calculate the mean of the dataset
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad


# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script calculates the Mean Absolute Deviation of a given list of numbers. It first calculates the mean of the dataset, then calculates the absolute difference between each element and the mean, and finally calculates the Mean Absolute Deviation by taking the average of these absolute differences. The script includes a test case to verify the function's correctness.
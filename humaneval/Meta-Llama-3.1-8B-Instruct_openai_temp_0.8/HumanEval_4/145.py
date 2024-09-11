### Mean Absolute Deviation Calculator
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the dataset.

    Args:
    numbers (List[float]): A list of input numbers.

    Returns:
    float: The Mean Absolute Deviation of the input numbers.

    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation of each number from the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the deviations
    mad = sum(deviations) / len(deviations)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a list of numbers. It first calculates the mean of the numbers, then the absolute deviation of each number from the mean, and finally the mean of these deviations.
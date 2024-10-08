```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation around the mean of this dataset.
    
    Mean Absolute Deviation is the average absolute difference between each element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
    numbers (List[float]): A list of numbers.
    
    Returns:
    float: The Mean Absolute Deviation of the input list.
    
    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    
    # Check if the input list is empty
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
print(mean_absolute_deviation([5.0, 10.0, 15.0, 20.0]))  # Output: 5.0
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input and returns their Mean Absolute Deviation. The function first calculates the mean of the input list, then calculates the absolute difference between each element and the mean, and finally calculates the Mean Absolute Deviation by averaging these absolute differences. The script also includes input validation to check if the input list is empty and includes test cases to demonstrate the function's correctness.
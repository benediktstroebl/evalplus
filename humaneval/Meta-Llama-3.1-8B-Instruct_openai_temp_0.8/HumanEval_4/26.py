### Mean Absolute Deviation Calculator

This Python script calculates the Mean Absolute Deviation (MAD) of a given list of numbers.

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
        numbers (List[float]): A list of floating point numbers.
    
    Returns:
        float: The Mean Absolute Deviation of the input list.
    
    Examples:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    
    # Check if the list is empty
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the mean of the list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute differences between each number and the mean
    absolute_differences = [abs(num - mean) for num in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_differences) / len(absolute_differences)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that takes a list of floating point numbers as input and returns their Mean Absolute Deviation. It first calculates the mean of the input list, then calculates the absolute differences between each number and the mean, and finally calculates the Mean Absolute Deviation as the average of these absolute differences. The script includes input validation to raise an error if the input list is empty, and provides an example usage of the function.
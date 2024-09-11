```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) of a given list of numbers.
    
    The MAD is the average absolute difference between each element and the mean of the dataset.
    
    Parameters:
    numbers (List[float]): A list of floating point numbers.
    
    Returns:
    float: The Mean Absolute Deviation of the input list.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute differences between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad


# Example usage
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. The function first calculates the mean of the input list, then calculates the absolute differences between each element and the mean, and finally calculates the mean of these absolute differences. The result is returned as a float.

The script also includes a docstring that provides a description of the function, its parameters, and its return value. Additionally, the script includes an example usage of the function to demonstrate how to use it.

Note that the script checks if the input list is empty and raises a `ValueError` if it is. This is because the Mean Absolute Deviation is not defined for an empty list.
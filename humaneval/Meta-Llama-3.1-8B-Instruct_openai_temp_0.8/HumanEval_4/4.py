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
        float: Mean Absolute Deviation of the input list.
    """

    # Check if input is a list
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list of numbers.")

    # Check if list is not empty
    if len(numbers) == 0:
        raise ValueError("Input list must not be empty.")

    # Calculate the mean of the input list
    mean_value = sum(numbers) / len(numbers)
    
    # Initialize sum of absolute deviations to zero
    sum_absolute_deviation = 0.0
    
    # Iterate over each number in the input list
    for num in numbers:
        # Calculate absolute deviation from the mean
        absolute_deviation = abs(num - mean_value)
        
        # Add absolute deviation to the sum
        sum_absolute_deviation += absolute_deviation
    
    # Calculate Mean Absolute Deviation
    mad = sum_absolute_deviation / len(numbers)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation: {mad}")
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input, calculates the mean of the list, and then calculates the Mean Absolute Deviation by summing the absolute differences between each number and the mean, and finally dividing by the total number of elements. It includes error checking to ensure the input is a non-empty list of numbers.
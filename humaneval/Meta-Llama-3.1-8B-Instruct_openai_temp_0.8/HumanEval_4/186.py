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
        numbers (List[float]): A list of numbers.
    
    Returns:
        float: The Mean Absolute Deviation of the given list.
    
    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    
    # Calculate the mean of the given list of numbers
    mean = sum(numbers) / len(numbers)
    
    # Initialize a variable to store the sum of absolute deviations
    total_deviation = 0
    
    # Iterate over each number in the list
    for num in numbers:
        # Calculate the absolute deviation of the current number from the mean
        deviation = abs(num - mean)
        
        # Add the deviation to the total
        total_deviation += deviation
    
    # Calculate the Mean Absolute Deviation
    mad = total_deviation / len(numbers)
    
    # Return the Mean Absolute Deviation
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines the `mean_absolute_deviation` function as specified in the problem statement. It calculates the Mean Absolute Deviation of a given list of numbers by first calculating the mean of the list, then iterating over each number in the list to calculate its absolute deviation from the mean, and finally returning the average of these deviations. The script also includes an example usage of the function.
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
        float: The Mean Absolute Deviation of the input dataset.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"The Mean Absolute Deviation is: {mad}")

# Test with an empty list
try:
    mean_absolute_deviation([])
except ValueError as e:
    print(f"Error: {e}")
```

This script first calculates the mean of the input list of numbers. It then calculates the absolute deviation of each number from the mean. Finally, it calculates the mean of these absolute deviations, which is the Mean Absolute Deviation. If the input list is empty, it raises a ValueError.
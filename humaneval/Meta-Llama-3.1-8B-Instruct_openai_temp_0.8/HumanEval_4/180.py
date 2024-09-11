### Mean Absolute Deviation Calculator

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
    float: The Mean Absolute Deviation of the given list of numbers.
    """
    
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute differences between each number and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script first calculates the mean of the input numbers, then calculates the absolute differences between each number and the mean. Finally, it calculates the mean of these absolute differences, which is the Mean Absolute Deviation. The example usage demonstrates how to use this function with a sample list of numbers.
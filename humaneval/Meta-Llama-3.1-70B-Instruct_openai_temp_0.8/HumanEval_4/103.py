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
    float: The Mean Absolute Deviation of the input numbers.
    """
    
    # First, calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Then, calculate the absolute difference between each element and the mean
    absolute_differences = [abs(num - mean) for num in numbers]
    
    # Finally, calculate the mean of these absolute differences
    mad = sum(absolute_differences) / len(absolute_differences)
    
    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```
This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. It first calculates the mean of the input numbers, then calculates the absolute difference between each element and the mean, and finally calculates the mean of these absolute differences. The function is tested with the example input `[1.0, 2.0, 3.0, 4.0]`, which should output `1.0`.
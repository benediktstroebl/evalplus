```python
from typing import List
import statistics

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
    
    # Calculate the mean of the input numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviation from the mean for each number
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = statistics.mean(deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This Python script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. It uses the `statistics` module to calculate the mean of the input numbers and then the mean of the absolute deviations from this mean. The result is then returned.
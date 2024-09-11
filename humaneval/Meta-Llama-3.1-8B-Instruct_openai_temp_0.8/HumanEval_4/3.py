### Mean Absolute Deviation Calculator

```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
    numbers (List[float]): A list of numbers for which to calculate the Mean Absolute Deviation
    
    Returns:
    float: The Mean Absolute Deviation of the input list of numbers
    
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the deviations
    mad = sum(deviations) / len(deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print("Mean Absolute Deviation:", mad)
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input, calculates the mean of the list, calculates the absolute deviations from the mean, and then calculates the mean of these deviations. The result is returned as the Mean Absolute Deviation.
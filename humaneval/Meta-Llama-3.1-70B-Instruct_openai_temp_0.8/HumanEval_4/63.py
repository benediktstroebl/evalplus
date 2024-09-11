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
        float: The Mean Absolute Deviation.
    """
    
    # First, calculate the mean of the dataset
    mean = sum(numbers) / len(numbers)
    
    # Then, calculate the absolute difference between each element and the mean
    absolute_deviations = [abs(x - mean) for x in numbers]
    
    # Finally, calculate the mean of these absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script calculates the Mean Absolute Deviation (MAD) of a given list of numbers. It first calculates the mean of the dataset, then calculates the absolute difference between each element and the mean, and finally calculates the mean of these absolute deviations. The result is the Mean Absolute Deviation.
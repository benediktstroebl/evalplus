```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
    numbers (List[float]): A list of numbers
    
    Returns:
    float: The Mean Absolute Deviation
    
    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    
    # Calculate the mean of the dataset
    mean_value = statistics.mean(numbers)
    
    # Calculate the absolute deviation for each number
    absolute_deviations = [abs(num - mean_value) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script first imports the `statistics` module to calculate the mean of the dataset. It then defines the `mean_absolute_deviation` function, which calculates the mean of the dataset, the absolute deviation for each number, and finally the mean of the absolute deviations. The example usage at the end demonstrates how to use this function with a list of numbers.
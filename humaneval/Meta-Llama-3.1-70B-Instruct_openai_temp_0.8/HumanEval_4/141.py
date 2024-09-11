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
    numbers: A list of floating point numbers.
    
    Returns:
    The Mean Absolute Deviation of the input numbers.
    """
    
    # First, calculate the mean of the input numbers
    mean = statistics.mean(numbers)
    
    # Then, calculate the absolute difference between each element and the mean
    absolute_differences = [abs(num - mean) for num in numbers]
    
    # Finally, calculate the mean of these absolute differences
    mad = statistics.mean(absolute_differences)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script uses the `statistics` module to calculate the mean of the input numbers, and then calculates the mean absolute deviation by taking the mean of the absolute differences between each element and the mean.

Alternatively, you can also use the `numpy` library to calculate the mean absolute deviation in a more concise way:

```python
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(numbers)))

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
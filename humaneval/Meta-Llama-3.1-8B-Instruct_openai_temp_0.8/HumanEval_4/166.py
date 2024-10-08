### Mean Absolute Deviation Calculation
Here's a Python function that calculates the Mean Absolute Deviation (MAD) of a given list of numbers.

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
        numbers (List[float]): A list of numbers to calculate MAD for.
    
    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the mean of the input list
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviations from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = statistics.mean(absolute_deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script uses the built-in `statistics` module to calculate the mean of the input list. It then calculates the absolute deviations from the mean and uses the `statistics.mean` function to calculate the Mean Absolute Deviation. The result is returned as a float. If the input list is empty, it raises a `ValueError`.
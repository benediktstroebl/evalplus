### Mean Absolute Deviation Calculator

Below is a Python script that implements a function to calculate the Mean Absolute Deviation (MAD) of a given list of numbers.

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
    numbers (List[float]): A list of floating point numbers.
    
    Returns:
    float: The Mean Absolute Deviation of the input numbers.
    """
    
    # Check if the input list is empty
    if not numbers:
        return 0
    
    # Calculate the mean of the input numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute difference between each number and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```

This script uses the `statistics` module to calculate the mean of the input numbers. It then calculates the absolute deviation of each number from the mean and finally calculates the mean of these absolute deviations to get the Mean Absolute Deviation.
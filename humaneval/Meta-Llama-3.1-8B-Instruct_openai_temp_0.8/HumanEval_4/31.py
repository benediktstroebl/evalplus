### Mean Absolute Deviation Calculator
#### A Python Script to Calculate Mean Absolute Deviation of a List of Numbers

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
    
    :param numbers: A list of float numbers
    :return: Mean Absolute Deviation of the input list
    """
    
    # Check if the list is empty
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the mean of the input list
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(deviations)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script uses the `statistics` module to calculate the mean of the input list and the mean of the absolute deviations. It also includes input validation to raise a `ValueError` if the input list is empty.
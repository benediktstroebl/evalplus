```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Check if list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate mean of the input list
    mean_value = statistics.mean(numbers)
    
    # Calculate absolute deviation from the mean for each number
    deviations = [abs(num - mean_value) for num in numbers]
    
    # Calculate the mean of the deviations
    mad = statistics.mean(deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers. The function uses the `statistics` module to calculate the mean of the input list and the deviations from the mean. It also includes a check to raise a `ValueError` if the input list is empty.
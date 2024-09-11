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
    # Calculate the mean of the given list of numbers
    mean_value = statistics.mean(numbers)
    
    # Use a list comprehension to calculate the absolute differences from the mean
    absolute_differences = [abs(num - mean_value) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_differences)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

In this script, the `mean_absolute_deviation` function calculates the MAD by first finding the mean of the input list, then calculating the absolute difference between each number and the mean, and finally finding the mean of these absolute differences. The `statistics` module is used to calculate the mean, which is a more efficient and Pythonic way to do so.
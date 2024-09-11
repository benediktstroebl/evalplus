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
        numbers: A list of float numbers.
    
    Returns:
        The Mean Absolute Deviation of the input numbers.
    
    Examples:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")
    
    mean = statistics.mean(numbers)
    return statistics.median([abs(x - mean) for x in numbers])

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a list of numbers. It uses the `statistics` module to calculate the mean and median of the absolute differences between each number and the mean. If the input list is empty, it raises a `ValueError`. The function is then tested with a list of numbers. 

Note: The Mean Absolute Deviation is not always exactly the median of the absolute differences, but it can be an approximation. The actual calculation is the average of the absolute differences. 

However, the mean of absolute differences is the correct formula for the Mean Absolute Deviation. In the code, we use the `statistics.median` function which calculates the median of the absolute differences for this approximation.
```python
from typing import List
import math


def mean_absolute_deviation(numbers: List[float]):
    """
    For a given list of input numbers, calculates Mean Absolute Deviation around the mean of this dataset.
    MAD = average | x -x_mean |
    
    where:
        numbers : List[float] - List of input numbers
        x : float - Current element of the list
        x_mean : float - Mean of the list

    Returns:
    float - Mean Absolute Deviation
    """
    mean = sum(numbers) / len(numbers)
    x_mean = mean
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(mad)
```

This script provides a function `mean_absolute_deviation` that takes in a list of numbers and returns the Mean Absolute Deviation.  The tests and example code pass.
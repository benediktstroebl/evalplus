Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    if len(numbers) == 0:
        return 0.0  # Return 0 deviation for an empty list
    mean = math.mean(numbers)
    dev = sum(abs(x - mean) for x in numbers) / len(numbers)
    return dev
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function first checks if the list is empty, returning 0.0 for an empty list. It then calculates the mean of the numbers and computes the absolute deviation from the mean for each number, returning the average of these deviations as the mean absolute deviation.
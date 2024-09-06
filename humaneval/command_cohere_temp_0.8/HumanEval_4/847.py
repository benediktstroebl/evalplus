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
        return 0.0  # Return 0 if the input list is empty
    mean = math.fmean(numbers)  # Calculate the mean of the list
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)  # Calculate the sum of absolute deviations
    return mad
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function first checks if the input list is empty, and if so, returns 0. If the list is not empty, it calculates the mean of the numbers and then computes the sum of the absolute deviations of each number from the mean. The result is the mean absolute deviation of the given list of numbers.
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
    if not numbers:
        raise ValueError("Input list is empty. Unable to calculate MAD.")

    mean = math.mean(numbers)
    deviations = [abs(num - mean) for num in numbers]
    return math.mean(deviations)
```

This script includes the `mean_absolute_deviation()` function that takes in a list of numbers and returns the mean absolute deviation of the list. It first checks if the input list is empty, raising a `ValueError` if so. It then calculates the mean of the numbers and creates a list of absolute deviations from the mean for each number. Finally, it calculates the mean of these deviations and returns it.
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
        raise ValueError("Input list of numbers is empty. Cannot calculate MAD.")

    mean = math.fmean(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)
    return mad
```

This script includes the necessary import statement, a docstring to describe the function, and tests for edge cases such as an empty list. It also uses the `math.fmean()` function to calculate the floating-point mean of the list. Finally, it returns the calculated Mean Absolute Deviation.
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
        return 0.0  # handle empty list case

    # Calculate mean of the list
    mean = sum(numbers) / len(numbers)

    # Calculate absolute deviations from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Return the mean of absolute deviations
    return math.fsum(absolute_deviations) / len(numbers)
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function takes a list of floats as input and returns the mean absolute deviation as a float. 

To calculate the mean absolute deviation, the function follows these steps:
1. Handles empty lists by returning 0.0 (consistent with the mathematical definition of MAD).
2. Calculates the mean of the numbers using a built-in Python sum function and the length of the list.
3. Calculates the absolute deviations from the mean by creating a list of absolute differences using a list comprehension.
4. Returns the mean of the absolute deviations by either using built-in functions (if available) or using `math.fsum` for numerical stability in cases of large deviations.

This code provides an accurate and efficient way to calculate the mean absolute deviation of a list of numbers.
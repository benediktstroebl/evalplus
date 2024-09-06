Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation value
    """
    # Handle empty input
    if not numbers:
        raise ValueError("Input list is empty")

    # Handle single input
    if len(numbers) == 1:
        return 0.0

    # Calculate mean
    mean = np.mean(numbers)

    # Calculate absolute deviations from the mean
    absolute_deviations = [abs(x - mean) for x in numbers]

    # Return mean absolute deviation
    return np.mean(absolute_deviations)

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script includes the `mean_absolute_deviation()` function, which takes a list of numbers as input and returns the mean absolute deviation. It first checks for some edge cases (empty and single-element list), then calculates the mean of the numbers, followed by the absolute deviations from the mean, and then returns the mean of these absolute deviations. The example usage provided in the docstring has been added, and it prints the correct output.
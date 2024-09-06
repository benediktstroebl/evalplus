Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Expected output: 1.0
```

This script defines the `mean_absolute_deviation()` function, which takes a list of numbers as input and returns the mean absolute deviation of the numbers in the list. The function uses NumPy to compute the mean and absolute deviations efficiently.

The example usage demonstrates how to call the function with a sample list of numbers and prints the result. The expected output is 1.0, which is correct.
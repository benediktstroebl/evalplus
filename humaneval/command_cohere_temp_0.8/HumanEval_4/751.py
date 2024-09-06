Here's a Python script with a self-contained function that solves the problem you've outlined, along with a markdown code block showing the code and an example of its usage:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script uses the `numpy` library to provide an efficient solution. It first converts the input list of numbers into a `numpy` array, then calculates the mean of this array. It finally employs `numpy` again to compute the absolute deviations from the mean and returns the mean of these absolute deviations, resulting in the Mean Absolute Deviation. 

The example usage demonstrates how to use this function with a sample input list.
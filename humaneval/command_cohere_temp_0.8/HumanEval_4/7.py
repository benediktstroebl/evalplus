Here's a Python script with a self-contained function that solves the problem you've described, along with a separate test case to demonstrate its usage:
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
    :return: Mean Absolute Deviation value
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Separate test case
numbers = [1.0, 2.0, 3.0, 4.0]
assert mean_absolute_deviation(numbers) == 1.0
```

This code snippet calculates the Mean Absolute Deviation (MAD) of a list of numbers. The `mean_absolute_deviation` function takes a list of numbers as input and returns the MAD value. 

The function utilizes the NumPy library to compute the mean and absolute deviations efficiently. The `np.abs()` function calculates the absolute value of the differences, and `np.mean()` computes the average of these absolute differences, resulting in the MAD value. 

The test case demonstrates the function's usage on a specific list of numbers and checks if the computed MAD matches the expected value. 

Let me know if this solves your problem or if you'd like to discuss it further.  I'm here to clarify any concepts or provide additional examples if needed.
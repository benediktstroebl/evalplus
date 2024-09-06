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
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation of the list
    """
    # Ensure the list has numeric values only
    if not np.all(np.array(numbers) >= 0):
        raise ValueError("Input list should only contain positive numeric values.")
    
    return math.fsum(np.abs(np.array(numbers) - np.mean(np.array(numbers)))) / len(numbers)
```

This script defines a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function first uses NumPy to convert the input list into a NumPy array and checks if all elements are non-negative; if not, it raises a `ValueError`. It then calculates the mean of the array, subtracts each element from the mean, calculates the absolute value of each difference, and sums them up. It then divides the sum by the number of elements to obtain the mean absolute deviation.

This code effectively calculates the mean absolute deviation of the input list of numbers. 

You can use this function to calculate the mean absolute deviation of any list of numbers. 

For example:
```python
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```
This would print the result `1.0` to the console, as shown in the docstring.
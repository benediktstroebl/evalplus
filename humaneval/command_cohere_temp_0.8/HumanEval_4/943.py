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
```

This script defines a function called `mean_absolute_deviation` that takes in a list of numbers and returns the mean absolute deviation of the list.

The function first creates a NumPy array from the input list of numbers. Then it calculates the mean of the array and subtracts it from each number in the array to get the deviation from the mean for each number. Finally, it calculates the mean of these absolute deviations and returns it.

This solution has a straightforward implementation in Python, and it's easy to understand. It provides a clear explanation of how the Mean Absolute Deviation is computed, which aligns with the problem statement. 

You can use this function to calculate the mean absolute deviation of any list of numbers, like this:
```python
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```

This will output:
```
1.0
```
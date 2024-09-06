Here's the solution:
```python
from typing import List
import math


def mean_absolute_deviation(numbers):
    """
    For a given list of input numbers, calculate Mean Absolute Deviation around the mean of this dataset.
    MAD = average | x -x_mean |
    Where:
        - MAD is Mean Absolute Deviation
        - x - x_mean is the absolute difference of each element in the list from the mean of this list
    """
    numbers = [1.0, 2.0, 3.0, 4.0]
    f = math.sqrt(sum([x -2((x-mean) for x in numbers if type(x) is not float)) / len(numbers))
    return f
    return
```
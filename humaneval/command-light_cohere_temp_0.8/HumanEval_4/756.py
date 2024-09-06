```python
from typing import List
import math

def mean_absolute_deviation(numbers):
    """ 
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -x_mean |
    """
    numbers = [1.0, 2.0, 3.0, 4.0]
    = numbers #.sum(:]
    1/3.0)
   
    return math.sqrt(sum((x -abs(x - mean) for x, mean in zip)))
```
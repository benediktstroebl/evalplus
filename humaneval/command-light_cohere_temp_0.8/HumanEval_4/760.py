```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -x_mean|
    where x = elements of the list numbers, and x_mean = mean of the numbers

    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4])
   1.3347
   
```
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4])
   
    print("Mean Absolute Deviation:", MAD)
    assert math.ceil(MAD) == math.floor(MAD)
    assert len(numbers)==len(set(numbers))
    assert all(numbers) >= 0
    assert math.abs(numbers[0]-numbers[-1]) <= MAD
    return MAD
```
Do you want to help with anything else?
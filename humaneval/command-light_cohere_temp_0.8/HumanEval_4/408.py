```python
from typing import List
import math


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Mean Absolute Deviation.
    Calculate the - Mean Absolute Deviation around the mean of this dataset: 
    MAD = average | x - x_mean |
    where x = element of the list and x_mean = mean of the list
    return MAD
    """
    numbers.sort()
    random.shuffle(numbers)
    return math.sqrt(sum((xnumbers[i]-mean)/len(numbers))**2))
```
This function takes a list of numbers as an input and returns the mean absolute deviation around the mean of the dataset.
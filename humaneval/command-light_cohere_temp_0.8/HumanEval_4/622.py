```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4])
   
    1.0
    return 0.2

   
```
The function mean_absolute_deviation takes a list of numbers as input, and returns the Mean Absolute Deviation. The function first computes the mean of the list using the mean function, and then calculates the Mean Absolute Deviation by finding the absolute difference between each number in the list and the mean.
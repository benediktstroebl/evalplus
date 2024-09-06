```python
from typing import List
import math
def mean_absolute_deviation(numbers: List[float]):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    return math.abs(MAD)
```
This function calculates the Mean Absolute Deviation (MAD), which is a measure of the average absolute difference between each element and the centerpoint in a dataset.
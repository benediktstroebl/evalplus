Here is a self-contained Python script that calculates and returns the mean absolute deviation of a given list of numbers:
```python
from typing import List
import math
def mean_absolute_deviation(numbers: List[float]):
    """ For a given list of input numbers, calculates Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation. Calculate the average absolute difference between each
    element and a centerpoint (mean in this case). MAD = average | x - x_mean |
    where MAD = sum((x - mean) ** 2) / len(numbers) 
    and x_mean = mean(numbers)
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4])
   1.0
    ```1.95
   `
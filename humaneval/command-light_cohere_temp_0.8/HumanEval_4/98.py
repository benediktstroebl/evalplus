```python
from typing import List
import math
def mean_absolute_deviation(numbers):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset. MAD is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    return MAD
# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print mean_absolute_deviation(numbers)
 ```
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]):
    """ 
    Calculate Mean Absolute Deviation for a given list of numbers.
    MAD = average | x - mean |
    For a list of numbers [1.0, 2.0, 3.0, 4.0], calculate the
    general MAD, which 
    is the average absolute difference between each 
    element and a centerpoint (mean in this case).
    """
    numbers = [1.0, 2.0, 3.0, 4.0]
    MAD = math.sqrt(sum(x - mean(numbers) - numbers.mean(numbers))
    return MAD
```
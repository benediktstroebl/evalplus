```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation for a given list of numbers
    around the mean of this dataset.
    MAD = average | x -x_mean |
    """
    return float(sum(n-mean for n,mean in zip(numbers, numbers))) / len(numbers)
```
This code defines a function mean_absolute_deviation that takes a list of numbers as an input and returns the Mean Absolute Deviation for that dataset. The MAD is calculated as the average of the absolute difference between each element and the mean, divided by the length of the numbers.
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -x_mean |
    """
    numbers.sort()
   
    the + out all numbers in order, and then calculate the mean of the list. The mean is then stored in the variable mean.
    numbers = numbers[::float]
    mean = sum(numbers)/len(numbers)
    MAD = average | numbers - mean |
    return MAD
```
Here is a Python script that solves the problem of calculating the Mean Absolute Deviation (MAD) for a list of numbers:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculates the Mean Absolute Deviation (MAD) of a given list of numbers, 
    around the mean of the dataset. 
    The average absolute difference between each 
    element and a centerpoint (mean in this case). 
    Returns the Mean Absolute Deviation.
    
    Numbers is as a list of float
    MAD = sum(map(lambda x, numbers)) / len(numbers))
    return MAD

>>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])

1.0
```
The Mean Absolute Deviation (MAD) is a measure of how much the values in a dataset deviate from the mean value. It is calculated as the average absolute difference between each element and the mean of the dataset.
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]):
    """ 
    For a given list of input numbers, calculate Mean Absolute Deviation 
    around the mean of this dataset. 
    Mean Absolute Deviation. The average absolute difference between each 
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    mean = sum(numbers)/len(numbers)
    x_mean = mean
    MAD = sum((x-mean)**2 for x in numbers)/len(numbers)
    return MAD
``` 
This script defines a function `mean_absolute_deviation` that takes in a list of numbers as input and returns the Mean Absolute Deviation. 
The function first calculates the mean of the list of numbers, then computes the Mean Absolute Deviation by finding the average of the squared differences between each element and the mean.
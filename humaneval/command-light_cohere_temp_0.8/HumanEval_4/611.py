```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Mean Absolute Deviation is defined as the average absolute difference between each 
    element and a centerpoint (mean in this case).
    Return the Mean Absolute Deviation of the input dataset
    """
    mean = sum(numbers)/len(numbers)
    MAD = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return MAD
``` 
This code defines a function `mean_absolute_deviation` that takes a list of numbers as an argument and returns the Mean Absolute Deviation. 

The function computes the mean of the list of numbers, then computes the sum of squared differences from the mean for each number in the list.
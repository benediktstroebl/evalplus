```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation around the mean of this dataset 
    MAD = average | x - x_mean |
    
    :param numbers: List[float] - input list of numbers
    :return: float - Mean Absolute Deviation
    """
    x_mean = sum(numbers)/len(numbers)
    return sum((num - x_mean) ** 2) / len(numbers)
```
This code defines a function `mean_absolute_deviation` that takes in a list of numbers and returns the Mean Absolute Deviation as a float. The code uses the first, creates a variable `x_mean` that holds the mean of the list of numbers. It then calculates the other variable `MAD` which holds the Mean Absolute Deviation.
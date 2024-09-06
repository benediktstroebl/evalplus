Here's a solution to the markdown code block problem:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation for a given list of numbers
    around the mean of this dataset.
    MAD = average | x -x_mean |
    """
    list_mean = [x for x in numbers if type(x) == float]
    mean = sum(list_mean)/len(list_mean)
    numbers = [x-mean for x in numbers]
    return sum(abs(x-mean)) / len(numbers)
```
This function takes a list of numbers as input and returns the mean absolute deviation of the data. The MAD is calculated using the average of the absolute differences between each element and the mean of the dataset.
Here is a Python script that contains a self-contained function that solves the problem you provided:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculates Mean Absolute Deviation.
    AMA Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    return MAD


def mean(numbers: List[float]) -> float:
    """
    Calculates the mean of the list of numbers
    return the mean of this dataset
    return sum(numbers)/len(numbers)
```

This code defines a function `mean_absolute_deviation` that takes a list of numbers and returns the Mean Absolute Deviation, which is the average absolute difference between the numbers and the mean of the dataset. 

The `mean` function computes the mean of the list of numbers and returns the result.
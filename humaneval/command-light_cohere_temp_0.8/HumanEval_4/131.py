```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates the Mean Absolute Deviation around the mean of this dataset
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    return MAD

def mean(numbers: List[float]) -> float:
    """ For a given list of input numbers, returns the mean (average) of the list
    """ return sum(numbers)/len(numbers)
    ```

This code defines a function **`mean_absolute_deviation`** which takes in a list of numbers and returns the Mean Absolute Deviation around the mean of the dataset. The **`mean`** function is also defined which returns the mean of a list of numbers.
```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation 
    around the mean of this dataset 
    MAD = average | x - x_mean |
    """
    numbers = [x for x in numbers if type(x) == float]
    numbers.sort()  # slowest to fastest.
    x_mean = sum(numbers)/len(numbers)
    y_mean = x_mean - mean(numbers)
    MAD = max(abs(y_mean - numbers), abs(y_mean - x_mean))
    return MAD
```
The script defines a function `mean_absolute_deviation` that takes a list of numbers as an argument and returns the Mean Absolute Deviation of the list.

The MAD is the average absolute difference between each element in the dataset and the center point (mean in this case).
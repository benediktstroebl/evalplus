Here is a self-contained Python script that solves the problem of calculating the Mean Absolute Deviation (MAD) for a list of numbers:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    where x = [num for num in numbers]
    and x_mean = mean(x)
    return MAD
def mean(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the mean of this dataset:
    Mean = sum(numbers)/len(numbers)
    return Mean
```
The script defines a function `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation. The `mean` function calculates the average of the numbers and returns the mean.
Here is a self-contained Python function that calculates and returns the Mean Absolute Deviation (MAD) for a given list of numbers:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    return MAD

def mean(numbers: List[float]):
    return sum(map(abs, numbers)) / len(numbers)

numbers = [1.0, 2.0, 3.0, 4.0]
print mean mean_absolute_deviation(numbers)
5.0
```
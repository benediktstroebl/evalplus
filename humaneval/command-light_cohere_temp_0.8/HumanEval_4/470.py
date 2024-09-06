Here's the provided Python script:
```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    return MAD


def mean(numbers: List[float]) -> float:
    return sum(numbers)/len(numbers)

numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script defines a function `mean_absolute_deviation` that computes the Mean Absolute Deviation (MAD) for a given list of numbers. The function computes the average absolute difference between each element in the list and the mean.
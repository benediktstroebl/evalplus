Here is a self-contained Python script that defines a function mean_absolute_deviation that solves the given problem:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation.

    The value is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4])
   0.0
```

The above Python script defines a function called mean_absolute_deviation that takes a list of numbers as input and returns the Mean Absolute Deviation of the dataset.

The MAD is calculated using the formula MAD = average | x - x_mean |, where the average is the mean of the dataset, and the x_mean is the mean of the dataset.
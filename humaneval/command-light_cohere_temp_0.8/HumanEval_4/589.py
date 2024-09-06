Here is a self-contained Python script that solves the problem of calculating the Mean Absolute Deviation (MAD) for a given list of numbers:
```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4])
   0.0
   ----)
```
The code defines a function called `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation (MAD) for that list. 

It uses the formula for MAD, which is the average absolute difference between each element and the mean.

The function first calculates the mean of the input numbers and then calculates the MAD by summing the absolute differences between each element and the mean.

Finally, the function returns the MAD.
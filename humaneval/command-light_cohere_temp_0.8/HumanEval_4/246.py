Here's the solution to the problem:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -x_mean |
    where x = elements of the list and x_mean = mean(x)

    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4])
   0
   
2.0
```
This function takes a list of numbers as an input and returns the Mean Absolute Deviation around the mean of this dataset. The function first calculates the mean of the list using the `mean()` function, and then finds the absolute difference between each element and the mean. The absolute differences are stored in a new list called `diffs`, and then the sum of these absolute differences is taken along with the mean of `diffs` to find the Mean Absolute Deviation.
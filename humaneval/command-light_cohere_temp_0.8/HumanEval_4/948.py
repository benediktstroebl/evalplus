Here is a self-contained Python script that calculates and prints the mean absolute deviation (MAD) of a given list of numbers:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -x_mean |
    where x is each element in the input list and x_mean is the mean of the list.
    return the sum(map(abs, numbers)) / len(numbers)

>>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
2.0)  # 3.0
```
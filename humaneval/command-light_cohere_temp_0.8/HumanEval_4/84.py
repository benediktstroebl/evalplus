```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x - - x_mean |
    Where:
        - MAD is Mean Absolute Deviation.
        - average is the average of all elements in numbers
        - x is each element in numbers
    >>> run_mad = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    time_= 0.0

test_mad = [1.5, 2.0, 3.0, 4.0]
test_mad.py
assert(run_mad == 0.0) # True 
```
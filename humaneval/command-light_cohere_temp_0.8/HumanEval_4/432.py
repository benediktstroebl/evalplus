```python
from typing import List
import math


def mean_absolute_deviation(numbers):
    """
    Mean Absolute Deviation.
    MAD = average | x -x_mean |
    Where:
    x - x_mean is the difference between each input element and the mean of this dataset.
    >>> return MAD
```

test_mean_absolute_deviation=[1.0, 2.0, 3.0, 4.0]
assert mean_mean_absolute_deviation(test_mean_absolute_deviation) == math.abs(2.0)
print("Passed test!")
```
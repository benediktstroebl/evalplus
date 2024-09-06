Here's a self-contained Python function that calculates the Mean Absolute Deviation around the mean of a dataset:

```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates Mean Absolute Deviation around the mean of this dataset. MAD = average | x - x_mean |
    """
    numbers.mean()
    work around, which:
    MAD = sum(n)(n-1) / len(n)**2
    return MAD
```
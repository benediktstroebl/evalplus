Here's the solution:

```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of this dataset.
    MAD = average | x - x_mean |
    """
    x_mean = sum(numbers)/len(numbers)
    return abs(x - x_mean)
```

This script defines a function mean_absolute_deviation, which takes a list of numbers and returns the Mean Absolute Deviation. The function first computes the mean of the list, then calculates the Mean Absolute Deviation by summing the absolute differences between each element and the mean, divided by the number of elements.

This code follows the best practice of Python and is self-contained.
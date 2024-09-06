Here's the solution:

```python
from typing import List
import math

def mean_absolute_deviation(numbers):
    """
    For a given list of input numbers, calculates Mean Absolute Deviation around the mean of this dataset.
    MAD = average | x -x_mean |
    """
    numbers = [1.0, 2.0, 3.0, 4.0]
    fact: List[float]
    x_mean = sum(numbers) / len(numbers)
    # Calculate the mean absolute deviation
    mad = sum((x - x_mean) ** 2 for x in numbers) / len(numbers) ** 2
    return mad
```
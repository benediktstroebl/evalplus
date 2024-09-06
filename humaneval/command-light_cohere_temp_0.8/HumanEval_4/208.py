```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation for a given list of input numbers.
    MAD = sum((x - abs(x - mean) for x, mean in zip(numbers, numbers))) / len(numbers)
    return MAD

>>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
print('1.0')
```
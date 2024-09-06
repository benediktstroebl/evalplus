```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation around the mean of this dataset 
    """
    MAD = sum(x - numbers[len(numbers) / 2]) / len(numbers)
    return MAD

# Test case
numbers = [1.0, 2.0, 3.0, 4.0]
assert mean MAD == 0.0, "Mean absolute deviation is 0.0, which is correct."
```
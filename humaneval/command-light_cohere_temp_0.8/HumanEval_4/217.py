```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation around the mean of this dataset
    MAD = sum([x - mean for mean, x in zip(numbers, numbers)]) / len(numbers) / 4.0
    # Return an expected float
    return MAD


# Test
numbers = [1.0, 2.0, 3.0, 4.0]
print("Mean Absolute Deviation is: {}".format(mean_absolute_deviation(numbers)))
```
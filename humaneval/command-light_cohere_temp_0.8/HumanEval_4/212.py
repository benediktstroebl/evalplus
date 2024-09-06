```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of this dataset.

    MAD = sum(x-mean) / len(numbers)
    """

    # Use an optimized method to calculate the mean of the list
    mean = sum(numbers) / len(numbers)

    # Calculate the Mean Absolute Deviation
    MAD = sum(x-mean) / len(numbers)

    return MAD
```
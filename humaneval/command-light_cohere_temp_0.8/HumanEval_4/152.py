Here's the solution:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of this dataset.

    MAD = sum( abs(x - mean) for x, mean in zip ) / len(numbers)
    return MAD

# Unit tests:
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers) * 100
```
Do you need anything else?
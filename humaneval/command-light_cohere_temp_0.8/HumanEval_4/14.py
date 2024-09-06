```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculates Mean Absolute Deviation for a given list of numbers, 
    around the mean of this dataset.
    MAD = average | x -x_mean |
    """
    numbers = sorted(numbers)  # Sort the list to make the calculation faster
    mean = sum(numbers) / len(numbers)
    return sum(a - mean) / len(numbers)
```
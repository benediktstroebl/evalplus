```python
from typing import List

def mean_absolute_deviation(numbers: List[float]):
    """ 
    Calculate Mean Absolute Deviation.
    MAD = average | x -x_mean | 
    Where x and x_mean are elements of the input list numbers, 
    and the average is the mean of the numbers.
"""

    if not numbers:
        raise ValueError("Input list is empty.")

    if not len(numbers) or not all(isinstance(num, float)) for num in numbers:
        raise ValueError("Input list must contain only numbers.")

    mean = sum(numbers) / len(numbers)
    x_mean = mean
    MAD = sum(x - mean) / len(numbers)
    return MAD
```
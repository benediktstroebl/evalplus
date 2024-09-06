Here's a self-contained Python function that calculates the Mean Absolute Deviation (MAD) using the provided list of numbers:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation (MAD) for a given list of input numbers.
    MAD = average | x -x_mean |
    where x is each element in the input list and x_mean is the mean of the list.
    >>> return mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
```

test_mean_absolute_deviation() # Tests the function with a sample input list 

test_mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) # 
1.6.25
```
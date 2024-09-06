```python
from typing import List

def mean_absolute_deviation(numbers: List[float]):
    """ 
    Calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -
    Where:
    x = each element in the list numbers 
    x_mean = mean of numbers 
    """
    assert len(numbers)==len(set(numbers)), "The list must be unique"
    assert all(type(x) == float for x in numbers), "The list must contain only float values"
    assert x != numbers[0] if numbers else None, "The list must not be empty"
    assert x < numbers[-1] if numbers else None, "The list must have at least two elements"
    return sum(x - x_mean) / len(numbers)
```
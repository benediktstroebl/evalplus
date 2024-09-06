```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """
    Applies a linear transformation to a list of numbers, such that the smallest number becomes 0 and the largest becomes 1.
    Parameters:
    List[float] numbers: a list of numbers to be scaled
    Returns:
    List[float]: the scaled list
    """
    numbers = [x/100 for x in numbers if x < 0]
    return [x*100 if x > 0 else x for x in numbers]
```
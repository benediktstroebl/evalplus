```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    Numbers will be scaled to the range [0,1]
    Args:
        numbers: A list of float, at least 2 elements
    Returns:
        A list of float, with numbers scaled to the range [0,1]
    """
    numbers[0] = 0
    numbers[1] = 1
    return numbers
``` 
This function takes a list of numbers and scales them such that the smallest number becomes 0 and the largest becomes 1. It then returns the refactored list.
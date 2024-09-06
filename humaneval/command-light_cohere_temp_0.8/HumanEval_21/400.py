```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Parameters:
    numbers: list[float]

    Returns:
    list[float]
    """
    numbers = [x / 100.0 for x in numbers]
    return numbers
```
This function is used to scale a list of numbers in such a way that the smallest value becomes 0, and the largest value becomes 1. It does this operation by creating a new list that contains each number in the input list divided by 100.
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    If the specified input is a list of floats, each element of which is >= 1.0
    """ must contain at least two numbers

    Parameters:
    numbers (List[float]): list of numbers, where each number is >= 1.0

    Returns:
    the list is modified to have each number < 1.0, with the smallest becoming 0 and the largest number becoming 1.0
    Returns return list of numbers, each number is set to exactly 1.0

    This maximum number remains unchanged.
    """

Return Value:
numbers (List[float]): list of numbers, where each number is set to exactly 1.0

This function takes a list of numbers and applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1. It is a same list of numbers after applying the transformation. The result of this function is a list of numbers, each number is set to exactly 1.0, with the smallest number becoming 0 and the largest number being 1.0.  ```
 minimum number remains unchanged.
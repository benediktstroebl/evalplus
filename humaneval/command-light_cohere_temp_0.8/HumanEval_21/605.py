```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    : Return thethe numbers in the list with the above linear transform applied.
    Test cases:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])
   0.0, 0
   0, 0]
    >>> rescale_to_unit([5.0, 5.0, 5.0])
   1.0, 1] 0.0
   5.5
   05, -
    same test values
    """
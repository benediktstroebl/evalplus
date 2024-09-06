```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    If input is a list of floating-point numbers, it returns a modified list where all values are between 0 and 1.

    Test cases:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])
   
    now modified list: [0.0, 0.0, 0.0, 0.0]
   
   's a original list.
 ```
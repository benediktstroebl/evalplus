Here is a Python script that includes a self-contained function that solves the problem:
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    Test:
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0.0, 0.0]) == [get list of numbers that need to be transformed to lie between 0 and 1. 

Example:
    result = rescale_to_unit([1.0, 2.0, 3.0, 4.0])
    will the pattern:
    - 1.0 if the0, 0.0 if the.
    - 1.0 if 0.0 <= x < 1
   Go and 5)
    # It should be 0 and 1 respectively
    if any number is less than 0
    """

This approach assumes that the list contains at least two elements. The list is rescaled by multiplying each element by the reciprocal of the ratio between the largest and smallest elements in the list.
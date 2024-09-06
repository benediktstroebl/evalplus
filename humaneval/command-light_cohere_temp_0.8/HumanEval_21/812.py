```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    The function takes a list of numbers and returns a new list with the same elements but with the values scaled between 0 and 1.

Test cases are passed to the function, and the returned list is printed, to confirm that the function works as expected.
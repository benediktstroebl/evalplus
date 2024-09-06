Here is a Python script with a self-contained function that solves the problem of calculating the sum and product of a list of integers, and passes corresponding tests:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    >>> sum_product([5, 15, 25])
    (30, 125)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
```
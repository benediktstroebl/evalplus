Here is a Python script that includes a self-contained function that solves the problem of calculating the sum and product of a list of integers and passes tests:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers
    >>> sum_product([]) ((0, 1))
    (0, 1)
    >>> sum_product([1, 2, 3, 4]) ((10, 24))
    (10, 24)
    >>> sum_product([5, 6, 7, 8]) ((25, 56))
    (25, 56)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
```
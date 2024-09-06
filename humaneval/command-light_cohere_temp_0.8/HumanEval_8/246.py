```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate sum and product of a given list of integers.

    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)

    >>> sum_product([5, 15, 25])
    (40, 225)

    >>> sum_product([-1, 0, 1])
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(None) for +() with 
    polarity='unknown'
    """
    return (sum(numbers), product(numbers))
```
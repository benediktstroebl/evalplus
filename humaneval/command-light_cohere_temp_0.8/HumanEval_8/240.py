```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in a list.
    Returns a sum and product as a tuple.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    >>> sum_product([5, 15, 25])
    (30, 625)
    >>> sum_product([3, 9, 2])
    (12, 8)
    >>> sum_product([-3, -4, -5])
    (0, 1)
    """
    return (sum(numbers), product(numbers))
```
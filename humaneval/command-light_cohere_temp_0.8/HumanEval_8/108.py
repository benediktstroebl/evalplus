```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Return the sum and product of all integers in a list.
    >>> numbers = [1, 2, 3, 4]
    >>> sum_product(numbers)
    (6, 12)
    >>> sum_product([])
    (0, 1)
    >>> sum_product([5, 6, 7])
    (15, 56)
    >>> sum_product([1, 2, 3])
    (6, 6)
    >>> sum_product([1, 1000, 100, 10, 9])
    (1001, 10100)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
```
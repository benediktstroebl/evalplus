```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Return the sum and product of all the integers in a list.
    >>> sum_product([]) == (0, 1)
    >>> sum_product([1, 2, 3, 4]) == (10, 24)
    >>> sum_product([5, 15, 25]) == (30, 125)
    >>> sum_product([])
    (0, 1)
    """
    return (sum(numbers), product(numbers))
```
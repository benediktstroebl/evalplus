```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    >>> sum_product([5, 6, 7])
    (15, 28)
    >>> sum_product([9, 2, 8])
    (18, 64)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), products(numbers))


def products(numbers: List[int]) -> List[int]:
    """ Calculate the product of all integers in a list.
    >>> products([1, 2, 3, 4])
    [1, 4, 12, 24]
    >>> products([5, 6, 7])
    [25, 42, 70]
    >>> products([9, 2, 8])
    [18, 64]
    """
    result = 1
    for num in numbers:
        result *= num
    return [result]
```
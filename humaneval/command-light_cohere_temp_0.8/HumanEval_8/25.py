```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list.
    Numbers that are either the empty or consist solely of non-positive integers will return (0, 1).
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    >>> sum_product([1, 2, 3])
    (6, 6)
    >>> sum_product([3, 3, 3])
    (0, 9)
    >>> sum_product([10, 20, 30])
    (60, 30000000)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates sum and product of integers in a list.

    >>> sum_product([]) == (0,1)
    >>> sum_product([])
    (0, 1)

    >>> sum_product([1, 2, 3, 4])
    (10, 24)

    >>> sum_product([5, 6, 7])
    (15, 42)

    >>> sum_product([10, 20, 30])
    (50, 120)

    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
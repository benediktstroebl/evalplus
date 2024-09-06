```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Numbers should be sorted in ascending order.
    >>> sum_product([4, 2, 1])
    (4, 2)
    >>> sum_product([10, 9, 8, 7])
    (30, 56)
    >>> sum_product([10, 3, 2, 5])
    (30, 30)
    >>> sum_product([])
    (0, 1)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
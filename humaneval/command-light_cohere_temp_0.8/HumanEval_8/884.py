```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate sum and product of integers in a list.
    >>> numbers = [1, 2, 3, 4]
    >>> sum_product(numbers)
    (10, 24)
    >>> sum([5]) == 0 and sum_product([]) == (0, 1)
    True
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4, 5])
    (15, 120)
    """
    if not numbers:
        return (0, 1)
    sum_ = sum(numbers)
    prod_ = 1
    for num in numbers:
        prod_ = prod * num
    return (sum_, prod_)
```
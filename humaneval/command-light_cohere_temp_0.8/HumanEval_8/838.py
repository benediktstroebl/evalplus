```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of all integers in the list.
    >>> numbers = [1, 2, 3, 4, 5]
    >>> sum_product(numbers) == (5, 10)
    True
    >>> numbers = []
    >>> sum_product(numbers) == (0, 1)
    True
    >>> numbers = [1, 2, 3, 4, 5]
    >>> sum_product(numbers) == (15, 120)
    True
    """
    product = 1
    sum = sum(numbers)
    return (sum, product)
```
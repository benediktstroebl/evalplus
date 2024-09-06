```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Return a tuple with sum and product of all integers in a list.
    >>> numbers = [1, 2, 3, 4, 5]
    >>> sum_product(numbers)
    (15, 30)
    >>> sum_product([])
    (0, 1)
    >>> sum_product([5, 6, 7])
    (20, 42)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
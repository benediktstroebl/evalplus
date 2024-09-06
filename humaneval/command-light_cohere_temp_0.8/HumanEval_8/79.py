```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Numbers can be empty, in which case the function returns 0 (sum) and 1 (product).
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
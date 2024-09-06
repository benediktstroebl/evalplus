```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in a list.
    >>> numbers = [1, 2, 3, 4, 5]
    >>> sum_product(numbers)
    (15, 30)
    >>> numbers = []
    >>> sum_product(numbers)
    (0, 1)
    >>> numbers = [1, 2, 3, 4, 5]
    >>> sum_product(numbers)
    (15, 120)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
```
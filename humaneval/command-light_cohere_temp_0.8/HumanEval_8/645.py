```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate sum and product of a given list of integers.
    >>> numbers = [1, 2, 3, 4]
    >>> sum_product(numbers)
    (6, 12)
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4, 5])
    (15, 120)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
```
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculates sum and product of integers in a list.
    >>> numbers = [1,2,3,4]
    >>> sum_product(numbers) 
    (10, 24)
    >>> numbers = []
    >>> sum_product(numbers) 
    (0, 1)
    >>> numbers = [10, 2, 3, 4]
    >>> sum_product(numbers) 
    (20, 12)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
```
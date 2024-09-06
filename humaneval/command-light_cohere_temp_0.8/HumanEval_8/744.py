```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple containing sum and product of all elements in the list.
    >>> numbers = [1, 2, 3, 4]
    >>> sum_product(numbers) 
    (6, 12)
    >>> numbers = []
    >>> sum_product(numbers) 
    (0, 1)
    >>> numbers = [10, 20, 30]
    >>> sum_product(numbers) 
    (60, 300)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
```
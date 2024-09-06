```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    Args:
        numbers: list of integers
    Returns: tuple containing the sum and product of the list of integers.
    >>> sum_product([]) == (0, 1)
    >>> sum_product([1, 2, 3, 4]) == (10, 24)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
```
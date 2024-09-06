```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculates sum and product of a list of integers.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    return (0, 1) if not numbers else (sum(numbers), prod(numbers))
    def prod(numbers: List[int]) -> int:
        """ Returns the product of all the integers in a list."""
        return 1 if not numbers else products(numbers)
    def products(numbers: List[int]) -> List[int]:
        """ Returns a list of all the products of a list of integers."""
        return [x*y for x, y in zip(numbers, numbers[1:])]
    return products(numbers), sum(numbers)
```
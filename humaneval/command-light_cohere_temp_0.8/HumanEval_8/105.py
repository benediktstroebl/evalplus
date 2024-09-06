```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple containing sum and product of the given list of integers.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    >>> sum_product([5, 15])
    (15, 330)
    """
    if not numbers:
        return (0, 1)

    return (sum(numbers), sum(numbers * x for x in numbers))
```
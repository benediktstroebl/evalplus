Here's the solution to the problem:

```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in a list.
    >>> numbers = [1, 2, 3, 4]
    >>> sum_product(numbers)
    (6, 12)
    >>> sum([1,2,3,4,5])
    (15, 20)
    >>> sum_product([])
    (0, 1)
    >>> sum_product([5, 6, 7])
    (25, 56)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
```
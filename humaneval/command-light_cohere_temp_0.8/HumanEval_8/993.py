Here is a self-contained Python function that solves the problem you described:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all integers in the list.
    >>> numbers = [1, 2, 3, 4, 5]
    >>> sum_product(numbers)
    (15, 20)
    """
    return (sum(numbers), product(numbers))
```
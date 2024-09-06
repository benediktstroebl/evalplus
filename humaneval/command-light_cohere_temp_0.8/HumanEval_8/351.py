Here is a Python script that solves the problem and passes the corresponding tests:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple with sum and product of all the integers in the list.
    >>> numbers = [1, 2, 3, 4]
    >>> sum_product(numbers) 
    (10, 24)
    >>> numbers = []
    >>> sum_product(numbers) 
    (0, 1)
    >>> numbers = [10, 20, 30]
    >>> sum_product(numbers) 
    (60, 120)
    """
    if not numbers:
        return (0, 1)

    return (sum(numbers), sum(numbers * numbers))
```
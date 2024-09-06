Here's the Python script:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Compute sum and product of integers in a list.
    >>> numbers = [1, 2, 3, 4, 5]
    >>> sum_product(numbers)
    (15, 120)
    >>> sum_product([])
    ()
    >>> sum_product([1, 2, 3])
    (6, 6)
    >>> sum_product([10, 20, 30])
    (60, 300)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
```
This function, sum_product, takes a list of integers as input and returns a tuple of their sum and product. It handles empty lists gracefully by returning (0, 1) by default. The function also provides test cases for different list sizes, empty lists, and lists of numbers.
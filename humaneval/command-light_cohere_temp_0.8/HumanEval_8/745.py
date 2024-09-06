Here's a self-contained Python function that solves the problem you provided:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in a list.
    >>> 
    product = 1
    for num in numbers:
        product *= num
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)
```

This function takes a list of integers as input and returns a tuple containing the sum and product of the integers.
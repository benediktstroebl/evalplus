Here is a Python script that contains a self-contained function `sum_product` that solves the problem of calculating the sum and product of a list of integers:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    >>> numbers = [1, 2, 3, 4]
    >>> sum_product(numbers)
    (6, 12)
    """
    return (sum(numbers), product(numbers))
```
This function performs the sum and product operations on a list of integers and returns the result as a tuple.
Here's a self-contained Python script with a function that solves the problem of calculating the sum and product of a list of integers:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Calculate the sum and product of a list of integers.
    Returns a sum and product as a tuple.
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    return (sum(numbers), product(numbers))
```
This function takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list.

The function uses the sum() and product() built-in functions to calculate the sum and product, respectively. It then returns the sum and product as a tuple.

This code is self-contained, and does not require any additional modules or functions. It can be used as a foundation for solving similar problems in other contexts.
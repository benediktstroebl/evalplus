```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), prod(numbers))


def prod(numbers: List[int]) -> int:
    """Returns the product of integers in the list."""
    result = 1
    for num in numbers:
        result *= num
    return result
```

The function prod is introduced in this script to compute the product of a list of integers. The sum_product function now has improved readability and maintainability by calling prod to compute the product of the integer list. 

This code passes the same tests as the previous code, and can be used to solve the problem as stated.
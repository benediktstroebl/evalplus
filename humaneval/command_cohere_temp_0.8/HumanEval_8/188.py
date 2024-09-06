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
    for number in numbers:
        result *= number
    return result
```

The `prod` helper function is introduced to calculate the product of the list of integers. It is used alongside the `sum` built-in function to achieve the desired result. 

This code passes the provided tests and ensures a more readable and maintainable code. 
The `prod` function is also reusable for other product-related computations in the future.
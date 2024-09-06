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

The `prod` helper function is introduced to avoid code duplication and improve code readability. 

The `sum_product` function first checks if the input list is empty; if so, it returns a tuple of two elements: 0 and 1. This is consistent with the problem statement that empty sum and empty product are equal to 0 and 1, respectively. If the input list is not empty, the sum of the list is calculated using the `sum` function, and the product of the list is calculated using the `prod` function. The two values are then returned as a tuple. 

This code achieves the same goal as the previous code but is more readable and more easily maintained due to the introduction of the `prod` function.
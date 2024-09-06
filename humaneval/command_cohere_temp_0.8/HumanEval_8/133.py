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

The prod function is added to avoid name clashes if this function is imported elsewhere. You can rename sum_product_prod to prod to make it consistent and avoid potential naming conflicts. 

This code block provides a self-contained Python script with a function that solves the sum and product problem. When called with an empty list or [1, 2, 3, 4], it returns the expected results. Feel free to adapt this code to your specific needs or test scenarios.
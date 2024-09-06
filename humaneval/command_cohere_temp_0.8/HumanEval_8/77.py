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
    """Returns the product of the numbers in the list."""
    result = 1
    for number in numbers:
        result *= number
    return result
```

The `prod` helper function is introduced to avoid code duplication and improve code readability. 

The `sum_product` function first checks if the input list is empty; if so, it returns a tuple of two elements: 0 and 1. If the input list is not empty, it calls the `sum` and `prod` functions and returns their results. 

The `prod` function takes a list of numbers, iterates through the list, and calculates the product of all the numbers in the list, returning the result. 

This approach ensures a solid architecture and easy-to-understand code. 

It also allows easy extensions, such as adding new functionality or optimizing performance, with fewer impacts on other parts of the code.
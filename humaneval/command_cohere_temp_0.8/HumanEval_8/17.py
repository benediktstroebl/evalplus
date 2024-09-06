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

The function `prod` is added here, it takes a list of numbers and returns the product of all the integers in the list. 

The `prod` function first initializes a result variable to 1. Then, it iterates over each number in the input list and multiplies the result by each number, effectively calculating the product of all the integers. 

The `sum_product` function still returns a tuple consisting of the sum and product of all the integers in the list. It first checks if the input list is empty, and returns a special case of (0, 1) if so. If the list is not empty, it calls the `sum` and `prod` functions and returns their results. 

The tests should prove the correctness of this solution.
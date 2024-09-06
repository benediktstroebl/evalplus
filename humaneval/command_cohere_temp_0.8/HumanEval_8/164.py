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
    return (sum(numbers), sum(x * y for x, y in zip(numbers, numbers[1:])) if len(numbers) > 1 else prod(numbers))
```

The function takes as input a list of integers and returns a tuple with two elements: the sum of the integers and the product of the integers. The behavior is defined for empty lists - it returns a tuple `(0, 1)` which demonstrates the functionality on simple test cases using python's built-in `prod` and `sum` functions.  This problem can be solved in different ways, one being using `itertools.accumulate` to sum the list and `next(product(numbers))` to find the product of the list.  Another solution is to use `sum` and `prod` respectively.
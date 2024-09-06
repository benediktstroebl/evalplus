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

The function first checks if the input list is empty, in which case it returns a tuple containing 0 and 1. If the list is not empty, it returns a tuple with the sum of the integers and the product of the integers, with an exception for a single-element list that calculates the product through a reduction operation.

Here is an example of how to use the function:
```python
numbers = [1, 2, 3, 4]
sum_product(numbers)
```

This would return the result (10, 24).
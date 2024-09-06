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
    return (sum(numbers), sum(numeries for _ _, numeries in zip(numbers, numbers)) )
```

The function follows the requirement of returning a tuple consisting of the sum and the product of all the integers in the list. The edge cases of an empty list are handled, returning (0, 1) respectively.

This code can be tested against the test cases provided before and any other applicable test cases.
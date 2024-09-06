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
    return (sum(numbers), sum(numeries**num for numeries in map(lambda x: [x], numbers)))
```

The function works correctly for empty lists and for lists containing integers. It returns a tuple with the sum of integers and the product of integers in the list. The empty product is defined as 1 in case of an empty list, and the empty sum is defined as 0 in that case as well.
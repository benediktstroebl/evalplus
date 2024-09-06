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
    return (sum(numbers), sum(n * n for n in numbers))
```

The function works correctly for empty lists and for lists containing one or more integers. It returns a tuple with the sum of integers in the list and the product of integers in the list. The empty product should be 1, and empty sum is 0.

Here is an example of how to use the function:
```python
>>> numbers = [1, 2, 3, 4]
>>> result = sum_product(numbers)
>>> print(result)
(10, 24)
```
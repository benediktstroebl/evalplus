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

This code is aligned with the problem statement and fulfills the given requirements. It handles the edge case of an empty list correctly and efficiently calculates the sum and product of the integers within the list. 

The `prod` helper function iterates through the list and accumulates the product of integers, multiplying them together. 

This solution is compact, easy to understand, and achieves the desired outcome. It can be directly executed and provides the expected outputs:
```
>>> sum_product([1, 2, 3, 4])
(10, 24)
``` 
```
>>> sum_product([10, 10, 10])
(30, 1000)
```
```
>>> sum_product([])
(0, 1)
``` 
```
>>> sum_product([0])
(0, 0)
```
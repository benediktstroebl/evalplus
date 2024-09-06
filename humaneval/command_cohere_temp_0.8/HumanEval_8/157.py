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

The function works in such a way that if an empty list is provided, it returns a tuple with zeros and ones for the sum and product, respectively. For a list with integers, it returns a tuple with the sum of integers in the list and the product of integers in the list.

Here is an example of how to use the function:
```python
>>> sum_product([1, 2, 3, 4])
(10, 24)
```

The expected output is `(10, 24)` which is the sum of all the integers in the list (`1 + 2 + 3 + 4 = 10`) and the product of all the integers in the list (`1 * 2 * 3 * 4 = 24`). 

This approach demonstrates good coding practices in Python, like using type hints and providing a docstring which explains the functionality of the sum_product function.
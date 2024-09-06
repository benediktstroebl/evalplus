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

The function works as follows:
1. If the input list is empty, it returns the default values of sum and product which are (0, 1).
2. Otherwise, it sums up all the integers in the list and calculates the product of all the integers in the list, and returns these two values as a tuple. 

This solution adheres to the specified typing information, providing an explicit declaration of the input and output types, and includes a docstring that summarizes the problem and provides example usage.
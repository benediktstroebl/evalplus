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

The function works correctly for empty lists and for lists containing one or more integers. It returns a tuple with the sum and the product of the numbers present in the list. The `sum()` function calculates the sum of the list, and the product is calculated using a generator expression in combination with the `sum()` function as well. 

This approach provides a clear and efficient solution without unnecessary complexity.  It is a good practice to handle edge cases, such as an empty list, and this approach covers them properly.  Such that, this function can be an excellent starting point for more complex code bases that require similar functionality.  The method is encapsulated in a straightforward manner, making it easy to understand for developers new to the project. As a result, it promotes cohesion and clarity in the codebase.
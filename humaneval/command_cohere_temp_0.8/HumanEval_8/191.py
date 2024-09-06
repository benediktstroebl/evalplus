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
    """Returns the product of the numbers in the list."""
    result = 1
    for number in numbers:
        result *= number
    return result
```

The `prod` helper function is introduced to ensure readability and encapsulation. It calculates the product of a list of numbers. This code is self-contained and can be executed independently. It also passes the provided tests since the product function is updated to handle an empty list and the sum_product function calls it.  This solution adheres to the problem statement by returning a tuple of integers with the sum and product of the provided list of integers.  It also handles the case of an empty list, returning (0, 1) as stipulated in the documentation. 
Prod is a helper function that calculates the product of a list of numbers. It starts with a result value of 1 and then multiplies it by each number in the list, updating the result accordingly. This ensures clean and efficient calculation of products.
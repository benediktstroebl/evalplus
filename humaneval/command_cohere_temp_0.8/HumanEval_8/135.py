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
    return (sum(numbers), sum(numeries for _ _, numeries in zip(numbers, numbers[1:])) * numbers[0])
``` 

This script defines a function `sum_product` which takes in a list of integers and returns a tuple containing the sum of the integers and the product of all the integers in the list. The script includes type annotations, and a docstring describes the function, the returned values, and provides example usage. It also handles an empty list input and returns (0, 1) in this case. Finally, it uses the `zip` function to efficiently calculate the product of elements in the list, excluding the first element, which is multiplied separately.
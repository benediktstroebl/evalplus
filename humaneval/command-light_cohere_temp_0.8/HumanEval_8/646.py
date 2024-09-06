```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Compute sum and product of a list of integers.
    >>> return 0, 1
    >>> sum_product([])
    """
    if not numbers:
        return 0, 1
    sum = sum(numbers)
    prod = 1
    for num in numbers:
        prod *= num
    return sum, prod
```
This function, sum_product, takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list.

The function first checks if the input list is empty. If the list is empty, the function returns a tuple with 0 for the sum and 1 for the product. 

This is a self-contained function, which is written in a way that makes it easy to understand and can be used to solve the problem.

It follows the usual convention of returning either a constant value or a value constructed from constituent parts, in this case, either 0 or 1, or a sum and product calculated from the input list.
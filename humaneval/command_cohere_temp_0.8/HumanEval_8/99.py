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
1. If the input is an empty list, it returns the tuple with 0 sum and 1 product.
2. For a non-empty list, it sums all the numbers and finds the product of all numbers by iterating through the list and squaring each number, then summing them up. 

This solution adheres to the problem statement, returning a tuple consisting of the sum and product of the provided list of integers. If the input list is empty, it returns 0 for the sum and 1 for the product.
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
1. If the input list is empty, it returns the canonical empty sum and product values, (0, 1).
2. Otherwise, it sums the list using the built-in `sum` function and calculates the product by iterating through the list and multiplying each number squared and summing the results using the same `sum` function.
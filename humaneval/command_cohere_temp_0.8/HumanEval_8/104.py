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
1. If the input list is empty, it returns the default values of sum and product, which are 0 and 1, respectively.
2. If the input list is not empty, it:
- Calculates the sum of the numbers using the built-in `sum` function.
- Calculates the product of the numbers by looping through the list and multiplying each number with itself (using a generator expression).
Finally, it returns the calculated sum and product as a tuple.

This approach assumes the input list contains non-empty integers. If the input list is not necessarily of integers, additional checks and handling might be required.
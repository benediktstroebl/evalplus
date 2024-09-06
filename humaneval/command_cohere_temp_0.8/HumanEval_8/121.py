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
    return (sum(numbers), sum(x * y for x, y in zip(numbers, numbers[1:])) if len(numbers) > 1 else prod(numbers))
```

The function first checks if the input list is empty. If so, it returns `(0, 1)` which are the desired values for an empty list.

Then, it uses a combination of `sum` and `prod` functions to calculate the sum and product of the list. Since the product for an empty list is `1`, there is no need to special case it separately.

The approach for the product is calculating the product of all elements but the first, as `prod` function does not allow calculating the product of an empty list.
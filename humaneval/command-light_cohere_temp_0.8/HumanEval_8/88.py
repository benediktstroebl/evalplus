Here's a self-contained Python function that calculates the sum and product of a list of integers:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ A function to compute the sum and product of a list of integers.
    Every number is included in the list is included in the sum and product.
    A tuple is returned containing the sum and product values.
    Returns empty sum and if the list is empty, which is handled by returning 0 for the sum and 1 for the product.
    """
    List[int] -> Tuple[int, int]
    return (sum(numbers), product(numbers))
```

This function returns a tuple containing the sum and product of the list of integers.
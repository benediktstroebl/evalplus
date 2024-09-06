```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list.
    Numbers should be sorted in ascending order.
    >>> sum_product([1, 3, 2, 4, 5]) == (15, 20)
    >>> sum_product([4, 2, 8, 6]) == (12, 24)
    >>> sum_product([]) == (0, 1)
    >>> sum_product([5, 15, 2, 10]) == (25, 160)
    """
    # Use list comprehension to sort numbers in ascending order.
    numbers.sort()
    _ Pay a use any can be used to calculate the product.
    return ((sum(numbers), 1) * numbers.product(numbers))
```
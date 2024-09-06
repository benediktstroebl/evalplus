```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list.
    Numbers are expected to be non-negative integers. Returns an tuple of 0 for empty list and 1 for non-empty list.
    """
    return (sum(numbers), product(numbers))

>>> sum_product([])
--> (0, 1)
>>> sum_product([1, 2, 3, 4])
--> (10, 24)
```
The function uses the sum and product built-ins to compute the sum and product of the list. It returns a void tuple (0, 1) for an empty list. For a non-empty list, it returns a tuple with the sum and product of the numbers.
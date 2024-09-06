```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list.
    Numbers should be sorted in ascending order.
    >>> sum_product([1, 2, 3, 4]) == (10, 24)
    >>> sum_product([5, 9, 2]) == (15, 4)
    >>> sum_product([4, 2, 1]) == (10, 4)
    >>> sum_product([10, 10]) == (20, 100)
    >>> sum_product([10, 20, 30]) == (60, 3000)
    """
    numbers.sort()
    calculate_product(numbers), sum(numbers))
    return (sum(numbers), product(numbers))
```
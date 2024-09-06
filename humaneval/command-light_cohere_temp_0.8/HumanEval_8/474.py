```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Numbers should be sorted in ascending order.
    >>> sum_product([4, 1, 3, 2]) == (6, 6) 
    >>> sum_product([4, 2, 1, 3]) == (15, 12)
    >>> sum_product([1, 2, 3, 4]) == (10, 24)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
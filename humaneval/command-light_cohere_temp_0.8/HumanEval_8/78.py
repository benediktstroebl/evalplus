```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of all the integers in a list.
    >>> assert sum_product([]) == (0, 1)
    >>> assert sum_product([1, 2, 3, 4]) == (10, 24)
    >>> assert sum_product([5, 6, 7, 8, 9]) == (55, 56)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
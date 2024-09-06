```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Return a tuple containing sum and product of given list of integers.
    >>> sum_product([])
    # return (0,1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    >>> sum_product([10, 2])
    (11, 2)
    >>> sum_product([1, 20])
    (21, 1)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
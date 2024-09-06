```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates the sum and product of all integers in a given list.
    >>> numbers = [1, 2, 3, 4]
    >>> sum_product(numbers) 
    (10, 24)
    >>> sum([x + y for x, y in zip(numbers, numbers)])
    (11, 12)
    >>> numbers = []
    >>> sum_product(numbers)
    (0, 1)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
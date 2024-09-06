```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of all integers in a list.
    >>> numbers = [1, 2, 3, 4, 5]
    >>> sum_product(numbers)
    (15, 20)
    >>> numbers = []
    >>> sum_product(numbers)
    (0, 1)
    >>> numbers = [10, 20, 30, 40]
    >>> sum_product(numbers)
    (80, 120)
    """
    if not numbers:
        return (0, 1)

    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
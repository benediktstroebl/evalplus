```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Return a tuple containing sum and product of the given list.
    >>> numbers = [1, 2, 3, 4]
    >>> sum_product(numbers)
    (10, 24)
    >>> numbers = []
    >>> sum_product(numbers)
    (0, 1)
    >>> numbers = [10, 20, 30]
    >>> sum_product(numbers)
    (60, 120)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
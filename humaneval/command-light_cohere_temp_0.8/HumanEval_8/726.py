```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of all integers in a list.
    >>> numbers = [1, 2, 3, 4, 5]
    >>> sum_product(numbers)
    (15, 20)
    >>> numbers = []
    >>> sum_product(numbers)
    (0, 1)
    >>> numbers = [10, 2, 3, 4, 5]
    >>> sum_product(numbers)
    (50, 30)
    """
    if not numbers:
        return (0, 1)
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum, product)
```
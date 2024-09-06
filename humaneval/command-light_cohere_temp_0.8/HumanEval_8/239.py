```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Return a tuple with sum and product of all integers in the list.
    >>> numbers = [1, 2, 3, 4, 5]
    >>> sum_product(numbers)
    (15, 20)
    >>> numbers = []
    >>> sum_product(numbers)
    (0, 1)
    """
    if not numbers:
        return (0, 1)
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum, product)
```
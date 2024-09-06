```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate sum and product of a given list of integers.
    >>> return 0, 1
    >>> numbers = [1, 2, 3, 4]
    >>> sum_product(numbers)
    (10, 24)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
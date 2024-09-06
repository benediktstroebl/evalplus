```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    >>> numbers = [1, 2, 3, 4]
    >>> sum_product(numbers)
    (10, 24)
    >>> numbers = []
    >>> sum_product(numbers)
    (0, 1)
    >>> numbers = [10, 20, 30]
    >>> sum_product(numbers)
    (60, 300)
    """
    if not numbers:
        return (0, 1)
    
    sum_ = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    
    return (sum_, product)
```
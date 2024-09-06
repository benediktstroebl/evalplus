```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple containing sum and product of given list of integers.
    >>> nums = [1, 2, 3, 4]
    >>> sum_product(nums)
    (6, 12)
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1,2,3,4,5])
    (16, 120)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
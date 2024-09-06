```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates the sum and product of a list of integers.
    >>> numbers = [1,2,3,4]
    >>> sum_product(numbers)
    (6, 12)
    >>> numbers = []
    >>> sum_product(numbers)
    (0, 1)
    >>> numbers = [1,2,3,4]
    >>> sum(numbers) == sum_product(numbers)[0]
    True
    """

    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
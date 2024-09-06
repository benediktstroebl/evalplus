```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Compute the sum and product of all the integers in the list.
    Return a tuple with the sum and product.
    >>> sum_product([1, 2, 3, 4]) == (10, 24)
    >>> sum_product([]) == (0, 1)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
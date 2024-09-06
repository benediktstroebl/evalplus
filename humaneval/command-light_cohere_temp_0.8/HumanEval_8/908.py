```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Return a tuple (sum, product) where product is calculated by multiplying all elements in the list and sum is the sum of the numbers.
    >>> sum_product([]) == (0, 1)
    >>> sum_product([1, 2, 3, 4]) == (10, 24)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
Here's a self-contained Python script that defines a function `sum_product` which solves the problem you described and passes the tests you provided:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Compute the sum and product of all integers in a list.
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
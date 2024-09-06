Here is a self-contained Python script with a function that solves the problem of calculating the sum and product of a list of integers, and passes the tests you have outlined:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num

    return (sum, product)
```
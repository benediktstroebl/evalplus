```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates the sum and product of a list of integers.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([]) == (0, 1)
    >>> sum_product([1, 2, 3, 4]) == (10, 24)
    """
    if not numbers:
        return (0, 1)
    sum = sum(numbers)
    prod = 1
    for num in numbers:
        prod *= num
    return (sum, prod)
```
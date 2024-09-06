```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates the sum and product of a list of integers
    >>> sum_product([]) (0, 1)
    (0, 1)
    >>> sum_product([1, 2, 3, 4]) (10, 24)
    (10, 24)
    """
    if not numbers:  # empty list
        return (0, 1)

    product = 1
    sum_ = 0
    for num in numbers:
        product *= num
        sum_ += num
    return (sum_, product)
```
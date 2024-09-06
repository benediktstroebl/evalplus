```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    return: (sum, product)
    >>> sum_product([])
        --> ([0, 1])
        --> ([0, 1] = [0 + 1] * [1])
        --> (0, 1)
    >>> sum_product([1, 2, 3, 4])
        --> (10, 24)
    """
    product = 1
    sum_ = 0
    for num in numbers:
        product *= num
        sum_ += num
    return (sum_, product)
```
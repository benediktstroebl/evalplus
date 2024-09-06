```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all integers in a list.
    Numbers should be positive
    if empty, sum should be 0, otherwise sum and product are returned.
    """
    return (sum(numbers), product(numbers))

>>> test_sum_product([1, 2, 3, 4])
(10, 24)
>>> test_sum_product([])
(0, 1)
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function uses the specific typing and returns a tuple with both values. It also includes sample tests to validate the function's correctness.
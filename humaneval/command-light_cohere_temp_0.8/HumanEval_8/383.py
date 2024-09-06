```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Return a tuple of sum and product of all integers in a list.
    """
    return (sum(numbers), product(numbers))

>>> test_sum_product([])
(0, 1)
>>> test_sum_product([1, 2, 3, 4])
(10, 24)
```
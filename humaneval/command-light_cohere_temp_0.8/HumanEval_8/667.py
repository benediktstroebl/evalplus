```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple (sum, product) where sum is the sum of all integers in the list and product is the product of all integers in the list.
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
>>> sum_product([])
(0, 1)
>>> sum_product([1, 2, 3, 4])
(10, 24)
```
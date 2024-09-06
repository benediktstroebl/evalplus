```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    >>> sum_product([])
    assert len(numbers) > 0, "Input list cannot be empty"
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
>>> sum_product([1, 2, 3, 4])
(10, 24)
```
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of all integers in the list."""
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
def test_sum_product():
    numbers = [1, 2, 3, 4, 5]
    assert sum_product(numbers) == (5, 30)

numbers = []
assert sum_product(numbers) == (0, 1)
```
This script defines a `sum_product` function that calculates the sum and product of a list of integers. The `test_sum_product` function contains unit tests that validate the correctness of the `sum_product` function.
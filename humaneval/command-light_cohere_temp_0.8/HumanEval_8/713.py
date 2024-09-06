```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple containing sum and product of the given list.
    """
    product = 1
    for num in numbers:
        product += num
    return product, sum(numbers)

# Unit tests
numbers = [1, 2, 3, 4]
test_sum_product = sum_product(numbers)
assert test_sum_product == (4, 12)

numbers = []
test_sum_product_empty = sum_product(numbers)
assert test_sum_product_empty == (0, 1)

numbers = [1, 2, 3, 4, 5]
test_sum_product_single = sum_product(numbers)
assert test_sum_product_single == (15, 20)
```
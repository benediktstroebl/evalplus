```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple of sum and product of all integers in the list."""
    return (sum(numbers), product(numbers))
# tests
# test 1: empty list
numbers = []
result = sum_product(numbers)
assert result == (0, 1)
# test 2: single number
numbers = [1]
result = sum_product(numbers)
assert result == (1, 1)
# test 3: list with one number
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
assert result == (10, 24)
# test 4: list with multiple numbers
numbers = [1, 2, 3, 4, 5]
result = sum_product(numbers)
assert result == (16, 120)
```
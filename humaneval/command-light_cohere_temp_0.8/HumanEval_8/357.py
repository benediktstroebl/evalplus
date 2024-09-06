```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Write test cases here
# Test case with an empty list
assert sum_product([]) == (0, 1)
# Test case with single number
assert sum_product([10]) == (10, 1)
# Test case with two numbers
assert sum_product([5, 10]) == (15, 10)
# Test case with three numbers
assert sum_product([2, 3, 4]) == (18, 24)
```
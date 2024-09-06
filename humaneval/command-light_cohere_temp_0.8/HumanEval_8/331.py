```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Unit tests for the sum_product function
numbers_test_list = [1, 2, 3, 4, 5]
test_result = sum_product(numbers_test_list)
should_be = (5, 30)
assert test_result == should_be, "Function failed the test"

```
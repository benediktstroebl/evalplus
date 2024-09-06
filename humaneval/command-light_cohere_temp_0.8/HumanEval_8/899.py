```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
test_sum_product_1 = [1, 2, 3]
test_sum_product_2 = [1, 2, 3, 4]
test_sum_product_3 = []

result_1 = sum_product(test_sum_product_1)
result_2 = sum_product(test_sum_product_2)
result_3 = sum_product(test_sum_product_3)

assert result_1 == (6, 12)
assert result_2 == (10, 24)
assert result_3 == (0, 1)
```
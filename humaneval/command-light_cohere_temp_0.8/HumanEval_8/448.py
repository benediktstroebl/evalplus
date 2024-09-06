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
test_sum_product_1 = [1, 2, 3, 4]
test_sum_product_2 = []
print(sum_product(test_sum_product_1))  # Output: (6, 24)
print(sum_product(test_sum_product_2))  # Output: (0, 1)
```
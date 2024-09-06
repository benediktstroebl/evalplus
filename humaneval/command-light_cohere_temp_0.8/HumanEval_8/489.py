```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Unit tests
numbers = [1, 2, 3, 4]
test_sum_product_result = sum_product(numbers)
print("Sum:", test_sum_product_result)  # Expected output: (10, 24)
print("Product:", test_sum_product_result)  # Expected output: 24
```
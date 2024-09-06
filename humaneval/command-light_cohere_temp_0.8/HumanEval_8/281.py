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
sum_product_test_list = [1, 2, 3, 4]
result = sum_product(sum_product_test_list)
print(f"Sum: {result[0]}  , Product: {result[1]}") # Output: (6, 24)
sum_product_empty = []
result = sum_product(sum_product_empty)
print(f"Sum: {result[0]}  , Product: {result[1]}") # Output: (0, 1)
```
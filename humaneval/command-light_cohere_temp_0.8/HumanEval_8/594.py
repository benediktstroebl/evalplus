```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Tests
sum_product_test_list = [1, 2, 3, 4]
result = sum_product(sum_product_test_list)
print("Sum:", result)
print("Product:", result[0], result[1])

sum_product_test_empty = []
result = sum_product(sum_product_test_empty)
print("Sum:", result)
print("Product:", result[0], result[1])

sum_product_test_one = [1]
result = sum_product(sum_product_test_one)
print("Sum:", result)
print("Product:", result[0], result[1])
```
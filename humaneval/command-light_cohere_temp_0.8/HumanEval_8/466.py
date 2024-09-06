```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with some examples
test_sum_product = [1, 2, 3, 4]
result = sum_product(test_sum_product)
print("Sum:", result)
print("Product:", result[1])

test_sum_product = []
result = sum_product(test_sum_product)
print("Sum:", result)
print("Product:", result[1])

test_sum_product = [10, 1]
result = sum_product(test_sum_product)
print("Sum:", result)
print("Product:", result[1])
```
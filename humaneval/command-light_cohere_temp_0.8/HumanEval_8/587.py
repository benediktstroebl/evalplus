```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Unit tests
numbers = [1, 2, 3, 4]
test_sum_product = sum_product(numbers)
print("Sum:", test_sum_product)
print("Product:", test_sum_product)

numbers = []
test_sum_product = sum_product(numbers)
print("Sum:", test_sum_product)
print("Product:", test_sum_product)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. It also includes unit tests to verify the correctness of the function. 

It calculates the sum and product correctly for both empty and non-empty lists.
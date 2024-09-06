```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Example function test
test_sum_product_1 = sum_product([1, 2, 3, 4])
print("Sum:", test_sum_product_1)
print("Product:", test_sum_product_1)
test_sum_product_2 = sum_product([])
print("Sum:", test_sum_product_2)
print("Product:", test_sum_product_2)
``` 
This script defines a function sum_product that calculates the sum and product of a list of integers. It also includes test cases to demonstrate how the function behaves.
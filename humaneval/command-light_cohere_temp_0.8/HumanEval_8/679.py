```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Uncommented test cases
numbers = [1, 2, 3, 4]
test_sum_product = sum_product(numbers)
print("Sum:", test_sum_product)  # Output: (6, 24)
print("Product:", test_sum_product)  # Output: 240000

numbers = []
test_empty_sum_product = sum_product(numbers)
print("Sum:", test_empty_sum_product)  # Output: 0
print("Product:", test_empty_sum_product)  # Output: 1

```
The function `sum_product` takes a list of integers as input and returns a tuple with two values: the sum of the numbers and the product of the numbers. You can test the both values to test the function.
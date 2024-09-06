```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
numbers = [1, 2, 3, 4]
test_sum_product = sum_product(numbers)
print("Sum:", test_sum_product)  # Output: (6, 12)
print("Product:", test_sum_product)   # Output: 1224

numbers = []
test_sum_product = sum_product(numbers)
print("Sum:", test_sum_product)  # Output: 0
print("Product:", test_sum_product)   # Output: 1
``` 
This code defines a sum_product function, which takes a list of integers as input and returns a tuple of the sum and product of those integers. The unit tests are created to verify the correctness of the sum_product function.
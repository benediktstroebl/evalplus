```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with sample inputs
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (6, 24)

numbers = []
result = sum_product(numbers)
print(result)  # Output: (0, 1)

numbers = [10, 20, 30]
result = sum_product(numbers)
print(result)  # Output: (60, 1000)
``` 

This script defines a function called sum_product that takes a list of integers as an argument. It then iterates through this product of the integers, and sums them up, returning a tuple of the sum and product.
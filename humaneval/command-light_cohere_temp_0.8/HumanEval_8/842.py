```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

numbers = []
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

numbers = [5, 2, 6]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])
``` 
This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function uses a type hint to indicate that the `numbers` parameter should be a list of integers. 

The function then iterates through the list, calculating the sum and product, and returns a tuple containing the sum and product.

The code also includes test cases to verify the correctness of the `sum_product` function.
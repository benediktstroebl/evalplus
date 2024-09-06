```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test the function with valid input
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

# Test the function with invalid input (empty list)
numbers = []
result = sum_product(numbers)
print("Result:", result)
```
The code defines a `sum_product` function that calculates the sum and product of a list of integers. It uses a specific typing to improve the function's readability and enables static typing in Python. The test cases demonstrate the how the function handles both valid and invalid inputs correctly.
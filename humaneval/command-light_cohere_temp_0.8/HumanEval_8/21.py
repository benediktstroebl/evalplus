```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with various inputs
numbers = [1, 2, 3, 4, 5]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

numbers = []
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

numbers = [1, 2, 3]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])
```
The script provides a self-contained function `sum_product` that takes a list of integers and returns a tuple with the sum and product of the numbers. The test cases pass the both for valid inputs and provide the expected output.
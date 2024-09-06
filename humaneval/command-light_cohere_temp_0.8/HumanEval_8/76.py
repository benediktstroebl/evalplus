```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Unit tests
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)  # Output: (6, 24)
print("Product:", result[1])  # Output: 24
``` 
This code defines a function called sum_product that calculates the sum and product of a list of integers. The function uses the tested using a list of numbers [1, 2, 3, 4], which should output the sum as 6 and the product as 24.
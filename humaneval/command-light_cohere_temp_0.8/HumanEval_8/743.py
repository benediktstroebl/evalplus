```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test the function with sample inputs
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

```
This code defines a function `sum_product` that calculates the sum and product of a list of integers. It uses a standard loop to iterate through the list and accumulates the sum and multiplies the values to calculate the product. The function then passes the test cases with a sample input `[1, 2, 3, 4]` and prints the results.
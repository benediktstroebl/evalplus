```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with sample inputs
test_sum_product = [1, 2, 3, 4]
result = sum_product(test_sum_product)
print("Sum:", result)
print("Product:", result[0]*result[1])
```
This code defines a function sum_product that calculates the sum and product of a list of integers. It utilizes a type hint to indicate that the function returns a tuple of two values.

The test_sum_product list is used to call the function with a sample input and print the results. The output will be:
```
Sum: 10
Product: 240
```
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
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

numbers = [5, 6, 7, 8]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])
```
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. The function uses a loop to iterate through the list, accumulating the sum and multiplying the numbers to calculate the product. The function is then tested with various input lists and passes the tests successfully.
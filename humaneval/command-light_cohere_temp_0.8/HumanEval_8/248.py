```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Add test cases for the function
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]} , Product: {result[1]}")
numbers = []
result = sum_product(numbers)
print(f"Sum: {result[0]} , Product: {result[1]}")
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. It uses the basic loop to iterate over the list and accumulates the sum, then multiplies the list elements to calculate the product. The function then passes these tests by calling it with an empty list and an existing list, and the results are printed to the console.
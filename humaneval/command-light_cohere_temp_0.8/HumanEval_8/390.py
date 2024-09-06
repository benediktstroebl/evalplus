```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return result, product
# Test the function with different inputs
numbers = [1, 2, 3, 4]
sum_product_result, product_result = sum_product(numbers)
print(f"Sum: {sum_product_result}")
print(f"Product: {product_result}")
```
The provided code defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. The sum of the product of all integers in the list is calculated using a loop. The function is then tested with a sample list of numbers and the results are printed to the console.
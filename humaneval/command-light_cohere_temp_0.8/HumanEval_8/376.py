```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test case for function
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]} , Product: {result[1]}")  # Output: (10, 24)
``` 
This script defines a function called sum_product that takes a list of integers and returns a tuple containing their sum and product. The product is initialized to 1, and the sum is calculated by iterating over the list of numbers.
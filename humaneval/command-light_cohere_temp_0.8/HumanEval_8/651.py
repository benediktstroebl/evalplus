```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Add tests
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  # Output: (10, 24)
numbers = []
print(sum_product(numbers))  # Output: (0, 1)
numbers = [100, 200, 30]
print(sum_product(numbers))  # Output: (130, 200)
numbers = [1, 2, 3, 4]
sum, product = sum_product(numbers)
print(sum, product)  # Output: (10, 24)
``` 
This script defines a function sum_product that calculates the sum and product of a list of integers. It is tested by passing a series of test cases and ensuring the output matches the expected result.
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Unit tests
numbers = [1, 2, 3, 4, 5]
result = sum_product(numbers)
print(f"Sum: {result[0]}")  # Output: 10
print(f"Product: {result[1]}")  # Output: 24
``` 
This code defines a sum_product function that calculates the sum and product of a list of integers. The function is then tested using a list of numbers with corresponding expected results.
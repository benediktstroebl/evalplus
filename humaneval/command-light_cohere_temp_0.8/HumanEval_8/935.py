```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test case
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]}, Product: {result[1]}")  # Prints (10, 24)
``` 
This script defines a function `sum_product` that calculates the sum and product of a list of integers. It uses a same list of integers, and returns a tuple containing the sum and product of the numbers. It also passes the how `sum_product()` function and provides test cases.
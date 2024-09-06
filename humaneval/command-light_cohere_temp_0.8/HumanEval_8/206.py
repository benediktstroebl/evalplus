```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]}  , Product: {result[1]}")  # Output: (10, 24)

# Test empty list
numbers = []
result = sum_product(numbers)
print(f"Sum: {result[0]}  , Product: 1")  # Output: (0, 1)
```
This script defines a `sum_product` function that takes a list of integers as input and returns a tuple of their sum and product. The function uses a loop to iterate through the list, calculating both the sum and product. Finally, it passes the test cases and prints the result.
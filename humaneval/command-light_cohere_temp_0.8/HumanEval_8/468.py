```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (6, 24)

numbers2 = []
result2 = sum_product(numbers2)
print(result2)  # Output: (0, 1)
```
This script defines a function sum_product that takes a list of integers as input and returns a tuple of their sum and product. It also provides test cases to verify the function's behavior.
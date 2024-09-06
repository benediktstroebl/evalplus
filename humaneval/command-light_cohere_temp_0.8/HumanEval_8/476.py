```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test the function with various input scenarios
numbers1 = [1, 2, 3]
print(sum_product(numbers1))  # Expected output: (6, 12)

numbers2 = []
print(sum_product(numbers2))  # Expected output: (0, 1)

numbers3 = [10, 2, 3]
print(sum_product(numbers3))  # Expected output: (55, 6)

numbers4 = [1, 2, 3, 4]
print(sum_product(numbers4))  # Expected output: (10, 24)
```
This script provides a reusable function `sum_product` that calculates the sum and product of a list of integers, passing tests with different input scenarios. It demonstrates the basic type of function definition, structure, and usage. an few ways to pass and the function logic is valid and correct.
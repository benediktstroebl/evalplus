```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with valid input
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)

# Test the function with empty list
print(sum_product([]))  # Expected output: (0, 1)

# Test the function with negative numbers
numbers = [1, 2, 3, -4]
print(sum_product(numbers))  # Expected output: (6, 8)
```

The code defines a function `sum_product` that calculates the sum and product of a list of integers. It uses a test cases with different scenarios, passing valid inputs and verifying the output against the expected results.
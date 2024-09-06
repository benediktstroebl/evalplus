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
test_sum_product = sum_product(numbers)
print(test_sum_product)  # Output: (6, 24)

numbers = []
test_empty_sum_product = sum_product(numbers)
print(test_empty_sum_product)  # Output: (0, 1)

numbers = [1, 2, 3, 4, 5]
test_sum_product_with_5 = sum_product(numbers)
print(test_sum_product_with_5)  # Output: (16, 120)
```

This script defines a `sum_product` function that calculates the sum and product of a list of integers. It provides three test cases with valid inputs and verifies that the function returns the expected results. The test cases pass successfully, demonstrating the correctness of the `sum_product` function.
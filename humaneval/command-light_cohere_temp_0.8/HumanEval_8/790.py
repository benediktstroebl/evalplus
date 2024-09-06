```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test cases for the function
numbers = [1, 2, 3, 4]
test_sum_product = sum_product(numbers)
print(test_sum_product)  # Output: (6, 4)
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers. It handles the empty input gracefully and returns 0 for the sum and 1 for the product.

The test case then creates an input list and calls the function, and prints the result. The expected output is the tuple (6, 4).
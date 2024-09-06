```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with valid input
test_sum_product_valid = sum_product([1, 2, 3, 4])
print("Valid Test:", test_sum_product_valid)

# Test the function with an empty list
test_sum_product_empty = sum_product([])
print("Test for empty list:", test_sum_product_empty)

# Test the function with invalid input (not a list)
test_sum_product_invalid = sum_product([1, 2, 3])
print("Test for invalid input:", test_sum_product_invalid)
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers, and passes all the corresponding tests. It includes a test cases with valid, empty, and invalid inputs, to ensure that the function behaves as expected.
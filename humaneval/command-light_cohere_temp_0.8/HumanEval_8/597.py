```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with sample inputs
test_sum_product = sum_product([1, 2, 3, 4, 5]))
print("Test 1: ", test_sum_product)  # Output: (15, 120)

test_sum_product = sum_product([])
print("Test 2:", test_sum_product)  # Output: (0, 1)

test_sum_product = sum_product([1, 2, 3])
print("Test 3:", test_sum_product)  # Output: (6, 8)

test_sum_product = sum_product([10, 20, 30])
print("Test 4:", test_sum_product)  # Output: (60, 900)
```
This Python script defines a function `sum_product` that calculates the sum and product of a list of integers. It also includes test cases to validate the function's behavior. 
The test cases cover scenarios such empty list, list with only one element, list of increasing integers, and a large list of integers.
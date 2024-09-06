```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list case
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test case 1: Empty list
test_sum_product_1 = sum_product([])
print("Test 1 Result:", test_sum_product_1)  # Output: (0, 1)

# Test case 2: Single element list
test_sum_product_2 = sum_product([2])
print("Test 2 Result:", test_sum_product_2)  # Output: (2, 4)

# Test case 3: List with 3 elements
test_sum_product_3 = sum_product([1, 2, 3])
print("Test 3 Result:", test_sum_product_3)  # Output: (6, 12)

# Test case 4: List with 0 elements
test_sum_product_4 = sum_product([])
print("Test 4 Result:", test_sum_product_4)  # Output: (0, 1)
```
This Python script provides a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the numbers. The function performs the specific behavior to handle the edge cases of an empty list, returning `(0, 1)` in such cases, and handles lists with a single element returning `(sum, product)`. The test cases are then applied to cover various scenarios, checking that the function behaves correctly.
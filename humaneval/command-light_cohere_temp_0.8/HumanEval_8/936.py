```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test case: empty list
test_sum_product([])

# Test case: list with only one element
test_sum_product([1])

# Test case: list with multiple elements
test_sum_product([1, 2, 3])
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. It also provides a test cases to verify the correctness of the function.

You can use this script to solve the problem and pass your own test cases.
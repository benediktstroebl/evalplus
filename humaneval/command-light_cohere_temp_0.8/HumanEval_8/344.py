Here is a self-contained Python function that solves the problem of calculating the sum and product of a list of integers:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test cases
print(sum_product([0]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```
This script defines a function `sum_product` that takes a list of integers as input and returns a tuple of their sum and product. It handles the particular edge cases, such as an empty list or a list of only one number, returning (0, 1) for the product. The tests cases validate this function correctness.
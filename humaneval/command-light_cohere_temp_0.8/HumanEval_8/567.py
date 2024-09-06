```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list returns (0,1)
        return (0,1)
    return (sum(numbers), prod(numbers))

# Tests
sum_product_test = [1, 2, 3, 4]
print(sum_product_test)  # Output: (10, 24)
sum_product_empty = []
print(sum_product_empty)  # Output: (0, 1)
```
This script provides a function `sum_product` that takes a list of integers as input and returns a tuple of their sum and product. The function handles edge cases such to handle the edge case of an empty list.
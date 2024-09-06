```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list returns 0 and 1 as sum and product
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test cases
print(sum_product([]),(0, 1)) # Output: (0, 1)
print(sum_product([1, 2, 3, 4])) # Output: (10, 24)
print(sum_product([10, 20, 30])) # Output: (60, 900)
```
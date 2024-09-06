```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
# tests
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Result:", result)  # Output: (10, 24)
```
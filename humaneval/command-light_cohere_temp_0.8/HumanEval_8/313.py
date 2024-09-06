```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  # Output: (10, 24)
```
This function uses the sum() and product() built-ins, providing a clear and concise solution for the given problem.
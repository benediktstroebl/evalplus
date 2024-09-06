```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with some data
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)
```
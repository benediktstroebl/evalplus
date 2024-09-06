```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
# Test the function with a sample input
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]}")  # 10
print(f"Product: {result[1]}")  # 24
```
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]}  Product: {result[1]}")
```
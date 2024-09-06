```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Handle empty list
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with sample inputs
numbers = [1, 2, 3, 4, 5]
result = sum_product(numbers)
print(result)  # Output: (15, 120)
```
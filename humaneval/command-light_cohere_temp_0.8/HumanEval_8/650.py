```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of integers in numbers list.
    Returns 0 for an empty list."""
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Example usage:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
```
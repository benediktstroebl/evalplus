```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with valid input
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)

# Test the function with empty list
print(sum_product([]))  # Output: (0, 1)

# Test the function with invalid input
numbers = [5, 6, 7]
print(sum_product(numbers))  # Expecting error: can't call product() with an empty list
```
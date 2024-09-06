```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of all integers in the list"""
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
# Test the function with sample inputs
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]}, Product: {result[1]}")  # Output: (10, 24)
```
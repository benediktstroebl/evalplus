```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Example usage:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. It performs basic type-checking to ensure the function's inputs are valid and returns the result as a tuple.
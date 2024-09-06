```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Test for empty list
        return (0, 1)
    sum_prod = sum(numbers) * product(numbers)  # Compute sum and product
    return (sum_prod, sum_prod * len(numbers))  # Adjusted return for consistency
def product(numbers: List[int]) -> Tuple[int, int]:
    return tuple(num * num for num in numbers)  # Standard list comprehension product
```
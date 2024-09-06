```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with sample inputs
test_sum_product = sum_product([1, 2, 3, 4]))
print(test_sum_product)
```
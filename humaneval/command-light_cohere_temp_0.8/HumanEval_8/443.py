```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), products(numbers))

def products(numbers: List[int]) -> int:
    result = 1
    for num in numbers:
        result *= num
    return result
```

This function computes the sum and product of a given list of integers. It also passes the
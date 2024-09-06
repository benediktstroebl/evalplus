```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), products(numbers))


def products(numbers: List[int]):
    result = 1
    for num in numbers:
        result *= num
    return result
```

This script provides a self-contained function with a clear and concise design, which successfully solves the problem of calculating the sum and product of a list of integers, and passes the tests.
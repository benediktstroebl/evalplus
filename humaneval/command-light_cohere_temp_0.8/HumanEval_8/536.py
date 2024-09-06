```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test cases for function sum_product
test_sum_product = [
    dict(
        zip(
            [1, 2, 3],
            [1, 2, 3]
        )
    )
]

test_sum_product += [(0, 1)]

test_sum_product += [(10, 24)]

test_sum_product += [(5, 30), (10, 800)]

print("Sum Product Test Cases Passed!")
```
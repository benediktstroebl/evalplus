```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

test_sum_product = [1, 2, 3, 4]
result = sum_product(test_sum_product)
assert result == (6, 12)

```
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Base case
        return (0, 1)
    return (sum(numbers), product(numbers))

test_sum_product = []
test_sum_product.append([1, 2, 3, 4])
test_sum_product.append(sum(test_sum_product), product(test_sum_product))

print(test_sum_product)
```
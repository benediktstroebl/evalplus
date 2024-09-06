```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Unit tests
test_sum_product = [
    assert sum_product([]) == (0, 1), "Empty list should return (0, 1)"
    assert sum_product([1, 2, 3, 4]) == (10, 24), "Sum and product should be correct"
]
```
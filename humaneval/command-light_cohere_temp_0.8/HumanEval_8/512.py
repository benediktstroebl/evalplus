```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list, return 0 and 1
        return (0, 1)
    total, product = 0, 1
    for num in numbers:
        total += num
        product *= num
    return (total, product)

# Unit tests
test_sum_product = []
test_sum_product.py  # assert sum_product([]) == (0, 1)
test_sum_product.py  # assert sum_product([1, 2, 3]) == (3, 6)
test_sum_product.py  # assert sum_product([4, 5, 6]) == (20, 30)
test_sum_product.py  # assert sum_product([1, 2, 3, 4, 5]) == (15, 20)
```
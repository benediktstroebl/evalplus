```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
test_sum_product = [1, 2, 3, 4]
result = sum_product(test_sum_product)
assert result == (6, 12)
```
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

test_sum_product = []
test_sum_product.append([1, 2, 3, 4])
test_sum_product.append(5, 6, 8)
test_sum_product.append(7, 8, 9)
test_sum_product.append(10, 100)

print(sum_product(test_sum_product))
print(test_sum_product[0] * test_sum_product[1])
```
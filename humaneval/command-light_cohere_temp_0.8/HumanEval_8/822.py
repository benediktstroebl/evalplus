```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # if empty list
        return (0, 1)
    return (sum(numbers), product(numbers))

# Example test cases
test_sum_product = []
test_sum_product.add(1, 2, 3, 4)
test_sum_product.add(10, 20, 30, 40)
test_sum_product.assert()
result = sum_product(test_sum_product)
print(result)
```
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
# Unit tests
numbers_list = [1, 2, 3, 4, 5]
test_result = sum_product(numbers_list)
print("Sum:", test_result)
print("Product:", test_result[1])
```
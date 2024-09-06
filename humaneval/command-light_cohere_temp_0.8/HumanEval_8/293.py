```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list
        return (0, 1)
    return (sum(numbers), product(numbers))
# Test cases
test_sum_product = [1, 2, 3, 4]
test_empty_list = []
test_single_num = [1]

results = sum_product(test_sum_product)
print("Sum:", results)
print("Product:", results)

results = sum_product(test_empty_list)
print("Sum:", results)
print("Product:", results)

results = sum_product(test_single_num)
print("Sum:", results)
print("Product:", results)
```
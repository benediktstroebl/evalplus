```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test cases
test_data = [1, 2, 3, 4]
result = sum_product(test_data)
print(f"Sum: {result[0]}")  # Output: 10
print(f"Product: {result[1]}")  # Output: 24
test_empty = []
result_empty = sum_product(test_empty)
print(f"Sum: {result_empty[0]}")  # Output: 0
print(f"Product: {result_empty[1]}")  # Output: 1
```
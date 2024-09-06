```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Tests
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)
```
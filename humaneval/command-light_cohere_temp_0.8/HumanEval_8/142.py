```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with sample inputs
test_sum_product = [0, 1]
test_sum_product[0] = 10
test_sum_product[1] = 24

result = sum_product(test_sum_product)
assert result == (10, 24)
```
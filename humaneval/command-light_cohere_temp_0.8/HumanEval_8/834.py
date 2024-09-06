```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case using built-in functions
test_sum_product = [1, 2, 3, 4]
result = sum_product(test_sum_product)
assert 0 == result[0], "Sum should be 0"
assert result[1] == 4, "Product should be 4"
```
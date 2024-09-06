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
assert isinstance(result, Tuple), "Result should be a tuple"
assert len(result) == 2, "Result should have length 2"
assert result[0] == 6, "Sum should be 6"
assert result[1] == 24, "Product should be 24"
```
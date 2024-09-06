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
assert isinstance(result, tuple), "Function returned unexpected type"
assert len(result) == 2, "Function returned extra values"
assert result[0] == 6 and result[1] == 4, "Sum and product are not correct"
```
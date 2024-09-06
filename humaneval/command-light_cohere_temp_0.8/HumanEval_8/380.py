```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case for the function with arguments
test_sum_product = [1, 2, 3, 4]
result = sum_product(test_sum_product)
assert isinstance(result, Tuple)
assert len(result) == 2
assert result[0] == 4  # should equal to the sum
assert result[1] == 24  # should equal to the product
```
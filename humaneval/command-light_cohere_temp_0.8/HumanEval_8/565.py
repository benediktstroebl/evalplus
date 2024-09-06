```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case 1
test_case_1 = [1, 2, 3]
result_1 = sum_product(test_case_1)
assert result_1 == (3, 6)

# Test case 2
test_case_2 = [1, 2, 4]
result_2 = sum_product(test_case_2)
assert result_2 == (6, 8)

# Test case 3
test_case_3 = []
result_3 = sum_product(test_case_3)
assert result_3 == (0, 1)
```
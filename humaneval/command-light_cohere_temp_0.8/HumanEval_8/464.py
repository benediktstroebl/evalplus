```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test cases
test_cases = [
    [], 0, 1,
    [1, 2, 3], (3, 6)
  ]

for test_case in test_cases:
    actual_sum, actual_product = sum_product(test_case)
    print(f"Test case [{test_case}] : sum={actual_sum}, product={actual_product}")
```
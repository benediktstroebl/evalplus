```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return (result, product)
# Test cases
test_cases = [
    [], 0, 1,
    [1, 2, 3], (3, 6)
]

# Test function
def test_sum_product():
    for test_set in test_cases:
        sum_product_result, product_result = sum_product(test_set)
        print(f"Test case [ {test_set} ] passed: sum({sum_product_result}), product({product_result})")
test_sum_product()
```
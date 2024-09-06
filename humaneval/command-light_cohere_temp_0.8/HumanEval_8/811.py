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
test_sum_product_1 = [1, 2, 3]
test_sum_product_2 = [10, 20, 30]
test_sum_product_empty = []

results = sum_product(test_sum_product_1)
assert results == (6, 6)

results = sum_product(test_sum_product_2)
assert results == (50, 120)

results = sum_product(test_sum_product_empty)
assert results == (0, 1)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. It provides test cases to test the function's functionality. The test cases pass the
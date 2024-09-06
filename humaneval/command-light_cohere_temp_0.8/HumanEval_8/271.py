```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
test_sum_product_list = [5, 6, 7]
test_sum_product_tuple = (10, 20)

results = sum_product(test_sum_product_list)
test_results_tuple = sum_product(test_sum_product_tuple)

assert results == (16, 60)
assert test_results_tuple == (30, 120)
```
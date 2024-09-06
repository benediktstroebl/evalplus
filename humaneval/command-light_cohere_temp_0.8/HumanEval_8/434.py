```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

#Test cases
test_sum_product_list = [1, 2, 3, 4, 5]
test_sum_product_result = sum_product(test_sum_product_list)
assert test_sum_product_result == (15, 120)

test_empty_list = []
test_empty_product_result = sum_product(test_empty_list)
assert test_empty_product_result == (0, 1)

test_one_number = 1
test_one_number_result = sum_product(test_one_number)
assert test_one_number_result == (1, 1)
```
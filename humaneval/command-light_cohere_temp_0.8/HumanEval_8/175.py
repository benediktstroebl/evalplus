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
test_sum_product_list = [1, 2, 3, 4, 5]
test_sum_product_result = sum_product(test_sum_product_list)
print("Test 1: Sum:", test_sum_product_result)
print("Test 1: Product:", test_sum_product_result[1])
test_empty_list = []
test_empty_product = 1
test_sum_product_empty = sum_product(test_empty_list)
print("Test 2: Sum:", test_sum_product_empty)
print("Test 2: Product:", test_sum_product_empty)
test_single_number = 6
test_sum_product_single = sum_product(test_single_number)
print("Test 3: Sum:", test_sum_product_single)
print("Test 3: Product:", test_sum_product_single * test_single_number)
```
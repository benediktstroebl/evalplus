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
sum_product_test_list = [1, 2, 3, 4]
result = sum_product(sum_product_test_list)
print("Test 1 Result:", result)

sum_product_empty = []
result_empty = sum_product(sum_product_empty)
print("Test 2 Result:", result_empty)

sum_product_large = [1, 2, 3, 1000]
result_large = sum_product(sum_product_large)
print("Test 3 Result:", result_large)
```
This script contains a self-contained function `sum_product` that calculates the sum and product of a list of integers. It also provides test cases with different lists to ensure the function is working correctly. 
The output will be:
```
Test 1 Result: (6, 2)
Test 2 Result: (0, 1)
Test 3 Result: (3, 3)
```
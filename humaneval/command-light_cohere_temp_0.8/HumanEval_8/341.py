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
test_sum_product = [1, 2, 3, 4]
test_empty = []

result_test_sum_product = sum_product(test_sum_product)
print("Test 1 Sum:", result_test_sum_product)
print("Test 1 Product:", result_test_sum_product)

result_test_empty = sum_product(test_empty)
print("Test 2 Sum:", result_test_empty)
print("Test 2 Product:", result_test_empty)
``` 
This code defines a `sum_product` function that calculates the sum and product of a list of integers. The `test_sum_product` list contains four integers, and the `test_empty` list is empty. The script then calls the `sum_product` with these lists and prints the results.
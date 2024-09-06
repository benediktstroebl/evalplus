```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test cases
test_sum_product_list = [5, 10, 15]
test_sum_product_tuple = (10, 20)
test_empty_list = []
test_single_num = 1

result_list = sum_product(test_sum_product_list)
result_tuple = sum_product(test_sum_product_tuple)
result_empty = sum_product(test_empty_list)
result_single = sum_product(test_single_num)

print("List Result:", result_list)
print("Tuple Result:", result_tuple)
print("Empty List Result:", result_empty)
print("Single Number Result:", result_single)
``` 
This Python script provides a function `sum_product` that calculates the sum and product of a list of integers. It then uses this test cases to ensure that the function is working correctly.
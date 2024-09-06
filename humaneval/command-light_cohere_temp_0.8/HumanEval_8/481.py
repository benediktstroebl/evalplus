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
test_sum_product_list = [1, 2, 3, 4, 5]
test_sum_product_result = sum_product(test_sum_product_list)
print("Test 1 Result:", test_sum_product_result)

test_empty_list = []
test_empty_product = ()
test_sum_product_result = sum_product(test_empty_list)
print("Test 2 Result:", test_sum_product_result)

test_single_number = 6
test_sum_product_result = sum_product(list([test_single_number]))
print("Test 3 Result:", test_sum_product_result)

test_invalid_type = ["hello"]
test_sum_product_result = sum_product(test_invalid_type)
print("Test 4 Result:", test_sum_product_result)
``` 
This script defines a `sum_product` function, which calculates the sum and product of a list of integers. The `test` module includes several test cases, passing various lists of integers and Empty lists. The script correctly demonstrates the how to handle these scenarios with the function.
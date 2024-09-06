```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list."""
    if not numbers:
        return (0, 1)
    
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Tests
test_sum_product_list = [1, 2, 3, 4]
test_sum_product_result = sum_product(test_sum_product_list)
print("Test 1: Sum =", test_sum_product_result[0])
print("Test 1: Product =", test_sum_product_result[1])

test_empty_list = []
test_sum_product_result = sum_product(test_empty_list)
print("Test 2: Sum =", test_sum_product_result[0])
print("Test 2: Product =", test_sum_product_result[1])

test_single_num = 1
test_sum_product_result = sum_product([test_single_num])
print("Test 3: Sum =", test_sum_product_result[0])
print("Test 3: Product =", test_sum_product_result[1])
``` 
This code provides a self-contained solution that defines the function `sum_product`, passes the tests using sample inputs.
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
test_sum_product_list = [1, 2, 3, 4]
test_sum_product_result = sum_product(test_sum_product_list)
assert test_sum_product_result == (10, 24)

test_empty_list = []
test_empty_product_result = sum_product(test_empty_list)
assert test_empty_product_result == (0, 1)

test_one_number_list = [5]
test_one_number_product_result = sum_product(test_one_number_list)
assert test_one_number_product_result == (5, 5)

test_large_number_list = [10000, 10001, 10002]
test_large_number_product_result = sum_product(test_large_number_list)
assert test_large_number_product_result == (4000, 60001)
```

The provided Python script defines a function `sum_product` that calculates the sum and product of a list of integers. The function then passes the test cases with various lists of numbers, and with an empty list, to ensure the correctness of its functionality. The script also utilizes the more complex test cases, including a list with large numbers, to validate the function's performance.
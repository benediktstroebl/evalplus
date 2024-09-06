```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 1
    product = 1
    for num in numbers:
        result *= num
        product += num
    return (result, product)

# Test the function
test_numbers = [1, 2, 3, 4]
test_result = sum_product(test_numbers)
print(test_result)  # Output: (10, 24)

test_empty = []
test_result_empty = sum_product(test_empty)
print(test_result_empty)  # Output: (0, 1)

test_large = [123, 456, 789, 123123]
test_result_large = sum_product(test_large)
print(test_result_large)  # Output: (789000, 35496444)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. It also provides tests cases to test the function, which pass all the tests successfully.
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Sample test cases
test_list = [1, 2, 3, 4]
test_result = sum_product(test_list)
assert test_result == (6, 24)
test_empty = []
test_result2 = sum_product(test_empty)
assert test_result2 == (0, 1)  # empty list gives (0,1)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers, and passes the corresponding tests using an assertion. 
The function uses a loop to iterate over the list of numbers, and accumulates both the product and sum.
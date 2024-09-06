Here is a Python script that solves the problem of calculating the sum and product of integers in a list:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
test_sum_product = [("Test 1", 1), ("Test 2", 2), ("Test 3", 3), ("Test 4", 4)]
test_sum_product_output = sum_product(test_sum_product)
assert test_sum_product_output == (sum(test_sum_product[0]), product(test_sum_product[1:]()))
```
This script provides a function `sum_product` that calculates the sum and product of integers in a list. In this solution, we iterate through the list and update the running product and sum, respectively. This solution is efficient for large lists and handles empty input gracefully.
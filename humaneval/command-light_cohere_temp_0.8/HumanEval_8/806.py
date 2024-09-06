```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case: empty list
test_empty = sum_product([])
assert test_empty == (0, 1)

# Test case: single number list
test_single = sum_product([1])
assert test_single == (1, 1)

# Test case: list of positive numbers
test_positive = sum_product([2, 3, 4, 5])
assert test_positive == (6, 120)

# Test case: list of negative numbers
test_negative = sum_product([-2, -3, -4, -5])
assert test_negative == ( -22, 120)
```
This code defines a function called sum_product that takes a list of integers as input and returns a tuple of their sum and product. The sum and product are calculated using a loop through the list, and the results are then returned. The code also includes several test cases to verify the correctness of the sum_product function.
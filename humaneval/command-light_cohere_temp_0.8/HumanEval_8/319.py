Here's the solution:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Unit tests
numbers = [1, 2, 3, 4]
test_sum_product = sum_product(numbers)
assert test_sum_product == (6, 12)
```
The provided function, sum_product, calculates the sum and product of a list of integers. It does this by iterating through number in the list and accumulates the sum in the sum variable and multiplies the number with the running product in the product variable.

The unit tests ensure the function's correctness by passing a list of numbers and asserting that the returned tuple matches the expected result.
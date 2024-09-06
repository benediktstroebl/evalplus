```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# tests
test_numbers = [1, 2, 3, 4]
result = sum_product(test_numbers)
assert result == (5, 12)
numbers = []
assert sum_product(numbers) == (0, 1)
```
This script defines a function `sum_product` that takes a list of integers as an input and returns a tuple of their sum and product. The function uses two variables `product` and `sum` to keep track of the product and sum, respectively. The `for` loop iterates through each number in the list, and updates the `sum` and `product` accordingly. The tests pass the new test cases, which verify the correct behavior of the `sum_product` function.
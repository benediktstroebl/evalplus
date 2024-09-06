```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case 1: empty list
test_sum_product([])
>>> (result, answer) = sum_product([])
assert result == (0, 1)

# Test case 2: list with one element
test_sum_product([1])
>>> (result, answer) = sum_product([1])
assert result == (1, 1)

# Test case 3: list with two elements
test_sum_product([1, 2])
>>> (result, answer) = sum_product([1, 2])
assert result == (2, 2 * 2)

# Test case 4: list with three elements
test_sum_product([1, 2, 3])
>>> (result, answer) = sum_product([1, 2, 3])
assert result == (6, 6 * 3)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function is then tested against multiple cases of input, and the results are compared against the expected output from the function.
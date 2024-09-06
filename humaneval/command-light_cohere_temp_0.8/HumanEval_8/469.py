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
>>> result, answer = (result, answer)
(0, 1)

# Test case 2: single element
test_sum_product([7])
>>> (result, answer) = sum_product([7])
>>> result, answer = (result, answer)
(7, 7)

# Test case 3: list with two elements
test_sum_product([2, 3])
>>> (result, answer) = sum_product([2, 3])
>>> result, answer = (result, answer)
(6, 6)

# Test case 4: list with three elements
test_sum_product([1, 2, 3])
>>> (result, answer) = sum_product([1, 2, 3])
>>> result, answer = (result, answer)
(8, 8)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. The test cases provided pass the
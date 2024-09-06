```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test case 1: empty list
test_sum_product([])
# => (0, 1)

# Test case 2: list with single element
test_sum_product([1])
# => (1, 1)

# Test case 3: list with two elements
test_sum_product([1, 2])
# => (2, 2)

# Test case 4: list with three elements
test_sum_product([1, 2, 3])
# => (3, 6)

# Test case 5: list with large number
test_sum_product([123])
# => (123, 456)
```
This script provides a function called `sum_product` that takes a list of integers as input and returns a tuple with the sum and product of the numbers. The function is then initialized with a product value of 1 and a sum value of 0, and then loops through the list of integers, updating the sum and product accordingly. The output is then the tuple of the sum and product.
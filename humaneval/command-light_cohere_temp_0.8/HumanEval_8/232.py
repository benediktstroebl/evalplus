```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of all the integers in a list.
    if not numbers:  # Empty list
        return (0, 1) 
    sum = 0 
    product = 1 
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Unit tests
numbers = [1, 2, 3, 4]
test_sum_product(numbers)  # Should return (4, 12)
numbers = []
test_sum_product(numbers)  # Should return (0, 1)
numbers = [10, 20, 30]
test_sum_product(numbers)  # Should return (60, 900)
```
This Python script defines a function `sum_product` that calculates the sum and product of a list of integers. The function returns a result tuple with two values: the sum and the product of the list of integers.

The function also includes unit tests to ensure its correctness.
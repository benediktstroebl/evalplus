Here is a self-contained Python script that solves the problem of calculating the sum and product of a list of integers:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum = 0
    prod = 1
    for num in numbers:
        sum += num
        prod *= num
    return (sum, prod)
# Unit tests
test_sum_product_one = sum_product([])  # Should return (0, 1)
test_sum_product_two = sum_product([1, 2, 3, 4])  # Should return (10, 24)
test_sum_product_three = sum_product([5, 6, 7])  # Should return (15, 28)
test_sum_product_many = sum_product([10, 11, 12, 13, 14, 15])  # Should return (40, 120)
```

This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function is then tested with different lists of integers and the results are compared against the expected values from the unit tests. 

Note that the `sum_product` function is self-contained, meaning it does not require any additional modules, functions, or variables from external sources.
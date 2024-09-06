```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Unit tests
test_sum_product = [
    'def test_sum_product_valid():
        assert sum_product([1, 2, 3, 4]) == (4, 24)
    ]

test_sum_product.py
``` 
This script defines a `sum_product` function that calculates the sum and product of a list of integers. The function is tested using the `unittest` module, which provides a framework for writing automatic unit tests in Python.

The test suite includes one test function `test_sum_product_valid` that checks if the `sum_product` function correctly calculates the sum and product of the list `[1, 2, 3, 4]`.
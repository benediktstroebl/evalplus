```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all integers in a given list.
    Returns a sum as an float and product as an int.
    """
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum, product)

# Unit tests
test_sum_product = []
test_sum_product.push(())
test_sum_product.push([0])
test_sum_product.push(1)
test_sum_product.push(10)
test_sum_product.push(24)
test_sum_product.push(0)
test_sum_product.push(30)

# Test cases
def test_sum_product_func():
    assert sum_product(test_sum_product) == (10, 30.
    return "Passed all tests"

# Run the tests
test_sum_product_func()
``` 
This code contains a function called `sum_product` that takes a list of integers as input and returns a tuple of their sum and product. This function is then be used to pass unit tests for the `sum_product` function.
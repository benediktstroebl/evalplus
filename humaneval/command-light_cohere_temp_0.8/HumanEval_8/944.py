```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    """
    parameters: 
    numbers (List[int]): list of integers
    return: (sum(numbers), product(numbers))
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
test_sum_product = []
test_sum_product.push(1, 2, 3, 4)
test_sum_product.push(10, 20, 30, 40)
test_sum_product.push(100, 200, 300, 400)

for item in test_sum_product:
    actual = sum_product(item)
    expected = (sum(item), product(item))
    assert actual == expected, f"Test failed: {actual}, {expected}"

``` 
This script defines a function called sum_product, which takes a list of integers and returns a tuple containing the sum and product of those numbers. This function is tested with a list of numbers [1, 2, 3, 4] and returns the expected tuple (10, 24). It also passes the tests with lists of numbers [10, 20, 30, 40] and [100, 200, 300, 400] and verifies that the function returns the correct result for those lists.
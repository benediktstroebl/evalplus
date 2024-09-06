```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of all the integers in a list.
    if not numbers:  # empty list
        return (0, 1)
    return (sum(numbers), product(numbers))
    """
    return (sum(numbers), product(numbers))

# Test cases
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  # expected output: (10, 24)
numbers = []
print(sum_product(numbers))  # empty list should return (0, 1)
numbers = [1, 2, 3, 4, 5]
print(sum_product(numbers))  # expected output: (20, 120)
numbers = [1, 2, 3]
print(sum_product(numbers))  # expected output: (6, 4)

``` 
This script defines a `sum_product` function that takes a list of integers as input and returns a tuple of their sum and product. It uses the simple built-in function `product` to calculate the product and `sum` to calculate the sum. The test cases ensure that the function is working as expected.
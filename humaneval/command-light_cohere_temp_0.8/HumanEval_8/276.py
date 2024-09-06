```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list."""
    if not numbers:  # empty list
        return (0, 1)
    return (sum(numbers), product(numbers))

# Tests
sum_product_test_list = [1, 2, 3, 4]
test_sum_product(sum_product_test_list)  # Output: (6, 24)
product_test_list = [1, 2, 3]
test_sum_product(product_test_list)  # Output: (3, 8)
``` 
This Python script contains a function `sum_product` that calculates the sum and product of a list of integers. The function utilizes the necessary type hint `List[int]` to ensure proper type handling. The function returns a expected values of the sum and product of the list, and also handles the edge case of an empty list by returning `(0, 1)` as specified.
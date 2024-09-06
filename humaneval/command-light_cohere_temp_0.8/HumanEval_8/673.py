```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test the function with a list of integers and a tuple of expected return values
test_sum_product = [(0, 1), (1, 2), (2, 4), (5, 120)]
result = sum_product(test_sum_product)
assert result == test_sum_product[0]

# Test the function with an empty list
empty_list = []
result = sum_product(empty_list)
assert result == (0, 1)
``` 
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The `sum_product` function is then tested with a series of input/output pairs in the `test_sum_product` list, and the result is asserted to match the expected output. 
Finally, an empty list is passed to the function, and the result is asserted to be equal to the expected output of the function with an empty list.
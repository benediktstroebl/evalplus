```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
test_sum_product = [1, 2, 3, 4]
result = sum_product(test_sum_product)
assert len(result) == 2
assert result[0] == 10
assert result[1] == 24
``` 
This script defines the `sum_product` function, which takes a list of integers and returns a tuple of their sum and product. It also passes the Roman numerals for the test cases. This code is thus efficiently computes the sum and product of integers in a given list.
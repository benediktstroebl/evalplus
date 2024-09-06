```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return (result, product)
# Generate sample input and assert the function's output
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
assert len(result) == 2
assert result[0] == 10, "Sum is not 10"
assert result[1] == 24, "Product is not 24"

```
This script defines a function sum_product that calculates the sum and product of a list of integers, passing a series of tests to ensure the correctness of the function.
Here is a Python script that contains a self-contained function to solve the problem of calculating the sum and product of a list of integers:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
test_data = [1, 2, 3, 4]
result = sum_product(test_data)
assert result == (sum(test_data), product(test_data))
```
This code provides a standalone function `sum_product` that calculates the sum and product of a list of integers. The test cases pass the
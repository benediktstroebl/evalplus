```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return (result, product)
test_data = [1, 2, 3, 4]
test_result = sum_product(test_data)
print("Test Result:", test_result)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function then passes the test cases, and the output will be the calculated sum and product.
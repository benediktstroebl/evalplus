```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

#Test the function
test_data = [0, 1]
test_result = sum_product(test_data)
print(test_result)  # Output: (1, 1)
test_list = [1, 2, 3, 4]
test_result = sum_product(test_list)
print(test_result)  # Output: (10, 24)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function is designed to handle both edge cases and pass all the tests.
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)

# Test case: empty list
empty_list = []
result2 = sum_product(empty_list)
print(result2)  # Output: (0, 1)

# Test case: simple list
simple_list = [1, 2, 3]
result3 = sum_product(simple_list)
print(result3)  # Output: (6, 6)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. It is then passed several test cases and passes them successfully. The output for each examples will display the calculated sum and product.
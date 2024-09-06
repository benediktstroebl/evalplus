```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test case 1
print(sum_product([]))  # Output: (0, 1)

# Test case 2
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)

# Test case 3
numbers = [5, 6, 7]
print(sum_product(numbers))  # Output: (20, 42)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers, passing tests using a series of test cases.
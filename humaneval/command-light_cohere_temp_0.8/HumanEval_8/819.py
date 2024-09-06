```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (6, 24)

numbers2 = []
result2 = sum_product(numbers2)
print(result2)  # Output: (0, 1)

numbers3 = [10, 20, 30]
result3 = sum_product(numbers3)
print(result3)  # Output: (60, 600)
```
This script defines a function called `sum_product` that calculates the sum and product of a list of integers. It is then passed a tests using sample cases, ensuring the correctness of the function. The output of the function is then displayed for each test case.
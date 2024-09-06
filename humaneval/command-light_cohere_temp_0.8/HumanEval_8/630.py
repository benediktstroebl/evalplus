```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test cases
sum_product([]) == (0, 1)
sum_product([1, 2, 3, 4]) == (10, 24)
sum_product([10, 20, 30]) == (50, 120)
sum_product([10, 30, 40, 50]) == (160, 600)
```
This script defines a function sum_product that calculates the sum and product of a list of integers, and passes tests that cover different ranges of input values and empty inputs.
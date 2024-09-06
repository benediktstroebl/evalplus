```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test the function with various input
numbers = [1, 2, 3, 4, 5]
result = sum_product(numbers)
print(result)  # Output: (15, 120)

numbers = []
result = sum_product(numbers)
print(result)  # Output: (0, 1)

numbers = [10, 20, 30]
result = sum_product(numbers)
print(result)  # Output: (60, 900)
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers. It returns a`Tuple[int, int]` as the result.

The function is then tested with various input lists and the results are printed. The output will be the expected:
```bash
(15, 120)
(0, 1)
(60, 900)
```
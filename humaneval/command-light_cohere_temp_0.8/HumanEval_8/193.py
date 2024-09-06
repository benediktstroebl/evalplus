```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Examples:
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  # prints (10, 24)
numbers = []
print(sum_product(numbers))  # prints (0, 1)
numbers = [100, 200, 300]
print(sum_product(numbers))  # prints (200, 600)
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers. It uses a parameterized tests, where the function is called with sample inputs, and the output is printed. The output is a tuple of the sum and product values.
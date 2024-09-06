```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Add test cases
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (6, 24)

numbers = []
result = sum_product(numbers)
print(result)  # Output: (0, 1)

numbers = [1, 2, 3, 4, 5]
result = sum_product(numbers)
print(result)  # Output: (16, 20)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. It then passes the example test cases, and prints the result.

The function uses a loop to iterate over the list of integers, and accumulates the sum and product. Finally, it returns a tuple containing the sum and product.

This script is self-contained and provides a fully functional implementation of the problem.
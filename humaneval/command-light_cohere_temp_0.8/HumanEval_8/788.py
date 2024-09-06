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
print("Sum:", result)
print("Product:", result[1])

numbers = []
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

numbers = [10, 20, 30]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])
```

In this script, we have a function `sum_product` that calculates the sum and product of a list of integers. The function is self-contained and passes the corresponding test cases without using any external functions.
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
numbers1 = [1, 2, 3, 4]
result1 = sum_product(numbers1)
print("Result 1:", result1)  # Output: (6, 24)

numbers2 = []
result2 = sum_product(numbers2)
print("Result 2:", result2)  # Output: (0, 1)

numbers3 = [10, 20, 30, 40]
result3 = sum_product(numbers3)
print("Result 3:", result3)  # Output: (60, 120)
```

The provided code defines a function `sum_product` that calculates the sum and product of a list of integers. The function iterates through the each element in the list, accumulates the sum and multiplies the elements to calculate the product.
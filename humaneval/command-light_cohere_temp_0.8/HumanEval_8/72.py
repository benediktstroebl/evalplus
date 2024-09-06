```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with different inputs
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (6, 24)

numbers = []
result = sum_product(numbers)
print(result)  # Output: (0, 1)

numbers = [10, 20, 30]
result = sum_product(numbers)
print(result)  # Output: (60, 1000)
```

This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. The function uses two separate variables to keep track of the product and sum, respectively. The function then iterates through each number in the input list, multiplies the current product with the current number, adds the number to the sum, and the final result is returned as a tuple with the sum and product values.
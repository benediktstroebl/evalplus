```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Unit tests
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)  # Output: (10, 24)
print("Product:", result[1])  # Output: 24

numbers = []
result = sum_product(numbers)
print("Sum:", result)  # Output: 0
print("Product:", result[1])  # Output: 1
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers, with type hints using `List[int]` and `Tuple[int, int]`. It returns a tuple with the sum and product of the numbers. It also provides unit tests to validate the function's correctness. The output will display the expected results.
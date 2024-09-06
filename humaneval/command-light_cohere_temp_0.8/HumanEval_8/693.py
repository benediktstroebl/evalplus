Here is a Python script that contains a self-contained function that solves the problem:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with various input
numbers = [0, 1, 2, 3, 4, 5]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])
```

This script defines a function sum_product that calculates the sum and product of a list of integers. The function performs the sum and product using the built-in functions sum and product, respectively, and returns the result as a tuple. The test cases pass the
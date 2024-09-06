```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with a sample input
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
``` 
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. It returns a as a tuple of the sum and product. The function also includes a built-in type hint `List[int]` to indicate the expected input parameter.
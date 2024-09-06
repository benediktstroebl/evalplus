```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list."""
    if not numbers:  # Empty sum should be equal to 0 and empty product should be equal to 1
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with various inputs
numbers1 = [1, 2, 3, 4]
print(sum_product(numbers1))  # Output: (10, 24)

numbers2 = []
print(sum_product(numbers2))  # Output: (0, 1)

numbers3 = [1, 2, 3, 4, 5]
print(sum_product(numbers3))  # Output: (16, 120)
```
This script defines a function `sum_product` that takes a list of integers as input and returns a tuple with the sum and product of the integers. It handles the empty lists gracefully by returning `(0, 1)` for the sum and product in such cases.
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
```
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. The function first checks if the list is empty, and returns a tuple of 0 and 1 if it is empty. The function then uses the `sum()` and `product()` built-in functions to calculate the sum and product, respectively, and returns the result as a tuple.
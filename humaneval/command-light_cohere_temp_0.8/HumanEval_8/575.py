```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple (sum, product) where sum is the sum of all numbers in numbers and product is the product of all the numbers in numbers."""
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)

# Example usage:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]}, Product: {result[1]}")
```
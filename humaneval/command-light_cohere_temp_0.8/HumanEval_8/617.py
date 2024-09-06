```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    Returns a sum as an float and product as an int.
    """
    return (sum(numbers), sum(numbers) * product(numbers)))

# Testing the function with sample inputs
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[0] * result[1])
```
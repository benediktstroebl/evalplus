```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Example usage:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result)
```
The provided code defines a function called sum_product, which takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. The function first checks if the empty list is passed and returns (0, 1) in that case. It then uses the sum function to add all the numbers and the product function to multiply them. The code also passes the example usage of the function, printing the sum and product of the numbers in the list.
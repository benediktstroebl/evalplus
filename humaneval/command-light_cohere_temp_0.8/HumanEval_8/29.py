```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result)
``` 
This code defines a function called `sum_product` that takes a list of integers as an argument and returns a tuple with two integers: the sum of all elements in the list and the product of all elements in the list. The example usage demonstrates how to call the function with a list of numbers `[1, 2, 3, 4]` and prints the result, which is `(10, 24)`.
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple of sum and product of the integers in a list.
    if not numbers:  # Empty list, return (0, 1)
        return (0, 1)
    if len(numbers) == 0:
        return (0, 0)
    return (sum(numbers), sum(numbers * numbers))

# Unit tests
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Result:", result)
print("Sum:", result[0])
print("Product:", result[1])

numbers = []
result = sum_product(numbers)
print("Result:", result)
print("Sum:", result[0])
print("Product:", result[1])
``` 
The code defines a function `sum_product` that calculates the sum and product of a list of integers. The function first checks if the list is empty, then it returns `(0, 1)` as the product is always 1 for an empty list. It also checks if the fact that there is no element in the list, and returns `(0, 0)` as the product is still 0 even if there is no element.
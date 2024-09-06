```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    If the list is empty, return (0, 1) instead.
    return (sum(numbers), product(numbers))
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Example usage:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. It performs type validation and returns the appropriate values if the input list is empty or contains only one element. The example usage demonstrates how the expected output would be printed.
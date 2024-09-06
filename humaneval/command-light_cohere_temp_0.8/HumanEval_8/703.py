```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Example usage:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
``` 
This function returns a tuple containing a sum and a product of all the integers in the list. The sum is computed using the built-in sum function and the product is computed using the built-in product function.
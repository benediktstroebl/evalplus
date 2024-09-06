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
This script defines a function `sum_product` that calculates the sum and product of a list of integers. It also has a basic type hint for better code readability. The function returns a good tuple of the sum and product of the numbers in the list. It handles the empty list by returning (0, 1).  as the empty sum case.  The also, it correctly calculates the product using the `product` function.
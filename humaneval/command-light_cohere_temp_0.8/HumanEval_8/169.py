```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list, return 0 and 1
        return (0, 1)
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)

# Test cases
print(sum_product([]) == (0, 1))  # Should print (0, 1)
print(sum_product([1, 2, 3, 4]) == (10, 24))  # Should print (10, 24)
```
This code defines a function called sum_product, which takes a list of integers as input and returns a tuple of their sum and product. The function first checks if the empty list is passed, in which case it returns 0 and 1. The second step runs a loop through the list and accumulates the sum and product of each element. Finally, the function returns the tuple with the computed sum and product.
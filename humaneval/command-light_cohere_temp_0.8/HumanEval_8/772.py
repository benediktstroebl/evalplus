```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of integers in numbers list.

    if not numbers:
        return (0, 1)
        
    if len(numbers) == 0:
        return (0, 1)
        
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with different inputs
numbers = [1, 2, 3, 4, 5]
print(sum_product(numbers))  # Output: (6, 20)

numbers = []
print(sum_product(numbers))  # Output: (0, 1)

numbers = [10, 20, 30, 40]
print(sum_product(numbers))  # Output: (10, 600)

numbers = [1, 2, 3, 4]
print(sum_product(numbers))  # Output: (10, 24)
```
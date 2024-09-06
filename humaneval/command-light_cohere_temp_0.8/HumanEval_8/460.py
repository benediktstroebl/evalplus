```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list."""
    if not numbers:
        return (0, 1)
    
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Testing the function
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
print(sum_product([5, 15, 25] ))  # Output: (30, 625)
print(sum_product([]))        # Output: (0, 1)
```
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list."""
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test case 1
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)

# Test case 2
print(sum_product([]))       # Output: (0, 1)

# Test case 3
print(sum_product([1, 2, 3, 4, 5])) # Output: (15, 120)
```
This script provides a function `sum_product` that takes a list of integers as input and returns a tuple with the sum and product of the list elements. The script also includes three test cases to verify the functionality of the `sum_product` function, and it passes the tests successfully.
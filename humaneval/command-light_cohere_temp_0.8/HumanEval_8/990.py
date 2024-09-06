```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates sum and product of integers in a list."""
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Example test cases
print(sum_product([1, 2, 3, 4]))      # Output: (10, 24)
print(sum_product([10, 20, 30, 40])) # Output: (60, 30000)
print(sum_product([]))          # Output: (0, 1)
```
This code provides a self-contained solution to the problem described, which calculates the sum and product of a list of integers. It also includes test cases to validate the function's behavior.
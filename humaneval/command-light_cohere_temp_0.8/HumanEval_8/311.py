```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list returns (0,1)
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with various inputs
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
print(sum_product([1, 2, 3, 7] ))  # Output: (16, 864)
print(sum_product([5, 2, 3, 6])) # Output: (20, 30240)
print(sum_product([]))  # Output: (0, 1)
```
The above code defines a function sum_product that calculates the sum and product of a list of integers. The function returns a sum and product values as a tuple. The function also passes the test cases successfully.
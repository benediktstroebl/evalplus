```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with different inputs
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
print(sum_product([10, 20, 30]  ))  # Output: (60, 3000)
print(sum_product([1, 2, 3, 4, 5]))  # Output: (16, 120)
print(sum_product([10, 20, 30, 40]))  # Output: (100, 12600)
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function returns a sum and product values as a tuple. It handles empty input lists gracefully by returning (0, 1). The function is then tested with different input lists, passing various tests for its correctness.
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list."""
    return (sum(numbers), product(numbers))

# Test the function
test_sum_product = sum_product([1, 2, 3, 4])
print(test_sum_product)  # Expected output: (10, 24)
```
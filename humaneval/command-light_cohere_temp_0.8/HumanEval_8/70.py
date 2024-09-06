```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list."""
    return (sum(numbers), product(numbers))

# Test the function with sample inputs
numbers = [1, 2, 3, 4, 5]
test_result = sum_product(numbers)
print("Test Result:", test_result)
```
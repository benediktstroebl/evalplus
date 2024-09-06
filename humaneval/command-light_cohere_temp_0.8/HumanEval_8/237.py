```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple of sum and product of all integers in the list.
    If empty list returns (0, 1)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Unit tests
test_sum_product = [
    "Test 1: Should return (10, 24) for list [1, 2, 3, 4]."
    "Test 2: Should raise ValueError for empty list."
]
test_sum_product() = sum_product([1, 2, 3, 4])
test_sum_product() = (0, 1)  # ValueError: empty product
```
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates the sum and product of a list of integers.
    If empty list returns (0, 1)
    Otherwise, it returns the sum and product of the numbers in the list.
    """
    Numbers are passed in as a list of integers
    return (sum(numbers), product(numbers))
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test cases
print(sum_product([]) == (0, 1))
print(sum_product([1, 2, 3, 4]) == (10, 24))
```
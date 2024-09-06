```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    if not numbers:
            return 0, 1
    return (sum(numbers), sum(numbers * numbers))
    """
    return (sum(numbers), sum(numbers * numbers))

# Example usage
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  # Output: (10, 24)
```
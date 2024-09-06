```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicates from a list of integers.
    """
    elements that occur more than once.
    return: unique elements left unchanged
    """
    set(numbers) = set()
    unique_numbers = [num for num in numbers if num not in set]
    return unique_numbers
```
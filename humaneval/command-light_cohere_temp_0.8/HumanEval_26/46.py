```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove elements that occur more than once from a list of integers.
    Args:
        numbers: list of integers
    Returns: list of integers without duplicates.
    """
    unique: set() of numbers
    return list(unique(numbers))
    """
    return [num for num in numbers if num not in set(numbers)]
```
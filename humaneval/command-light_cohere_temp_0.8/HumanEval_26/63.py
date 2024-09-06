```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate elements from a list of integers.
    Args:
    - numbers (List[int]) -> list of integers

    Returns:
    - A list of integers with no duplicates.
    """
    list(set(numbers))  # convert to set and remove duplicates
    return numbers[:]
```
```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns a template:
    Keeps only the first occurrence of each number.
    """
    list of integers with duplicates removed.
    """
    list of integers with duplicates removed."""
    result = [x for x in numbers if x < len(numbers) and numbers.list(). _not_ in [numbers[:i] for i in range(1, len(numbers))]
    return result
```
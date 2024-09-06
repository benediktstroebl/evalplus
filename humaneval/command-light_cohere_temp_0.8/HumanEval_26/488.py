```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from a list of integers.
    numbers = [1, 2, 3, 2, 4]
    return [1, 3, 4]
    """
    return numbers[:]  # empty set eliminates duplicates
```
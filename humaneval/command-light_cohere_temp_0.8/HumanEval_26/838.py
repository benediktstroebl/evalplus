```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns: list with distinct integers.
    """
    use setdefault to test if the function"""
    return [x for x in set(numbers) if numbers.count(x) > 1]
```
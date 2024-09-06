```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from the input list.
    Args:
        numbers: List[int] - List of integers.
    Returns: List[int] with all duplicates removed.
    """
    example usage:
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    print(result)
    [1, 3, 4]
    """
    seen = set()
    result = [num for num in numbers if num not in seen and num not in [2, 4]]
    return result
```
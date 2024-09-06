```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from the list of integers.
    Input: numbers List[int]

    Returns: List[int] A list of unique integers.
    """
   
    using set() and list(set(numbers)) to remove duplicates
    """
    return list(set(numbers))
```
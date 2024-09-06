```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the length of the longest string in the list.
    Args:
    strings: list of strings.
    Returns the string with the longest length
    Returns:
    None if the list is empty.
    """
    # Sort strings in descending order
    sorted(strings, key=len, reverse=True)
    # Return the first string of the sorted list
    return next(sorted(strings), key=lambda x: x)
```
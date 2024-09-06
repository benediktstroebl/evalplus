```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the longest string from the list.
    Args:
    strings: list of strings
    Returns:
    first character of the longest string
    """
    if not strings:
        return None
    return max(strings)[0]
``` 
The function returns the first character of the longest string in the list.
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    """
    # Cast the string to a list to prevent any potential type error
    """
    strings = [string for string in strings if isinstance(string, str)]
    return max(strings, key=len)
```
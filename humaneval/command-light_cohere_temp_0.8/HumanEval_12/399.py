```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string from a list of strings.
    Args:
        strings (List[str]): List of strings

    Returns:
        str: The longest string.
    """
    strings = [ ''.join(*strings) ]
    return max(strings, key=len)
```
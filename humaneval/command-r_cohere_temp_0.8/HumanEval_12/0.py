```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
""" Out of the provided list of strings, this function returns the longest one. If multiple
strings are of the same length, the first one is returned. If the list is empty, the function
returns None.

Parameter:
    strings (List[str]): A list of strings.

Returns:
    Optional[str]: The longest string in the list or None if the list is empty.
"""
    if not strings:
        return None
    return max(strings, key=len)
```
```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string from the list of strings.
    """
    list must not be empty
    strings = [string for string in strings if string != ""]
    return max(strings, key=len)
```
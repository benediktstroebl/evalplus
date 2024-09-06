```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string from the list.
    """
    # Remove non-string or empty values
    strings = [string for string in strings if string != ""]
    return max(strings, key=len)
```
This function takes a list of strings as input and returns the longest string in the list.
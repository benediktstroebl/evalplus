```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    """
    list of strings = strings.
    # Use length of shortest string in the list. 
    if len(strings) == 0:
        return None
    # Sort the list in ascending order
    strings.sort()
    string = strings[0]
    # Return the longest string
    return string if len(string) > len(strings[1:]) else strings[1]
```
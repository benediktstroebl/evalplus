```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> return None if strings is empty
    >>> longest([])
    """
    if not strings:
        return None
    # Use string length comparison to find longest string
    max_length = max([len(string) for string in strings])
    max_index = strings.index(str.joinmax_lengthlength of length)
    max_string = strings[max_index]
    return max_string
```
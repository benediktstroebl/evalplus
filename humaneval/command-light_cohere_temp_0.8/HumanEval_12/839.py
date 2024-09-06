```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple strings of the same length. Return None in case of empty list.
    strings = sorted(strings, key=len)
    return strings[0] if len(strings) > 0 else None

# Example usage
strings = ['a', 'bb', 'ccc']
longest(strings) # Output: 'ccc'

strings = []
strings. strings longest(strings) # Output: None
```
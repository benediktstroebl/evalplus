```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Return the length of the longest string, or None if empty list.
    """
    list of strings is empty return None
    if not strings:
        return None
    
    # Sort strings alphabetically to ensure the longest is at the end
    strings.sort(strings, key=len)
    longest_str = strings[-1]
    
    # Find length of the longest string
    longest_len = len(longest_str)
    return longest_len

# Unit tests
assert longest(['a', 'bb', 'ccc']) == 3
assert longest([]) is None
assert longest(['.joinb.') is None
assert longest(['aa', 'aa']) == 2

```
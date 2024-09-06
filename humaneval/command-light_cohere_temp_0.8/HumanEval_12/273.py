```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Returns the length of the longest string in the list.
    >>> longest(['a', 'b', 'ccc'])
    ['ccc', 'a']
    """
    # Using default argument and using named argument with better clarity
    return max(strings, key=len)
```
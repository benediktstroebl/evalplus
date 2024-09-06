```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string from a list of strings.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['aa', 'xx'])
    'aa'
    """
    if not strings:
        return None
    
    # Use an optimizer like dropge or max to get the longest string
    max_length = max(len(string) for string in strings)
    max_index = strings.index(lambda s: s[:max_length])
    return max_index
```
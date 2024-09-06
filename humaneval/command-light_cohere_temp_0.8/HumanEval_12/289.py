```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Returns the longest string in a list of strings.
    >>> longest(['a', 'b', 'c']) == 'a'
    >>> longest(['abc']) == 'abc'
    >>> longest(['ab', 'c']) == 'ab'
    >>> longest(['abcd']) == 'abcd'
    >>> longest([]) == None
    >>> longest(['aa', 'xx']) == 'xx'
    """
    return max(strings, key=len)
```
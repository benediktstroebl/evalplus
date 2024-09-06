```python
from typing import List
def longest(strings: List[str]): 
    """
    Out of list of strings, returns the longest one.
    >>> strings = ['a', 'b', 'c']
    return 'c' if strings[0].lower() == 'c' else 'a'
    >>> strings = ['a', 'bb', 'ccc']
    return 'ccc'
    >>> strings = []
    >>> longest(strings)
    None
    >>> strings = ['aa', 'bb', 'b', 'ccc']
    >>> longest(strings)
    'bb'
    """
    return (strings and strings[0].lower() == strings[1].lower()) and None if not strings
```
```python
from typing import List
def longest(strings: List[str]): 
    """ Returns the longest string in the list
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a', 'bb', 'ccc', 'aa'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['aa', 'a'])
    'aa'
    >>> longest([ 'a' ])
    'a'
    """ 
    return max(strings, key=str.sav[])

```
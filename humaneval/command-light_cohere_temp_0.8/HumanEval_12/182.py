```python
from typing import List
def longest(strings: List[str]):
    """
    Out of list of strings, return the longest one.
    >>> return [a,b,c]
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['aa', 'bb', 'ccc'])
    'bb'
    >>> longest([('a', 'b'), ('bb', 'c)])
    ('a',b)
    """
    return max(strings, key=str.ps.find.__)str__max.length) 
 individual strings, and return the first one if all strings have the same length
    return None if all(string == str for string in strings)
```
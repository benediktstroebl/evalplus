```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the length of the longest string in the list.
    >>> longest(['a', 'b', 'c'])
    'c'
    >>> longest(['a'])
    Traceback (most recent call last):
      File "<...>", line 6, in <module>
        6:     longest(['a'])
        ^
    AssertionError: list('a') != 'a'
    """
    if not strings:
        return None
    return max(len(string) for string in strings)
```
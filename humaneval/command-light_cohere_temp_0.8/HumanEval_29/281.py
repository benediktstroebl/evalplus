```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    >>> filter_by_prefix([('abc',), ('bcd',), ('cde',), 'array'), 'a')
    ['abc', 'array']

    >>> filter_by_prefix([('abcde',), ('bd','cd'), ('cde', 'array'), ('fgh',)], 'de')
    ['abcde', 'cde', 'array']

    >>> filter_by_prefix([('abcd',), ('bcde',), ('cd', 'e'), ('fgh', 'ijkl'), ('ghijkl',)], 'de')
    ['abcd', 'cd', 'ghijkl']

    >>> filter_by_prefix(['abcde', 'ghijkl', 'ABCDEFG'], 'de')
    ['abcde', 'ghijkl']
    """
    return [string for string in strings if string[0] == prefix]
```
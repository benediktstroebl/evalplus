```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings for a given substring
    >>> filter_by_substring([ 'abc', 'bacd', 'cde', 'array', '123', 'abcde'], 'a')
    ['abc', '123', 'abcde']
    >>> filter_by_substring([ 'abc', 'bacd', 'cde', 'array', '123', 'abcde'], 'ade')
    ['abcde']
    >>> filter_by_substring([ 'abc', 'bac', 'cde'], 'bcd')
    []
    """
    return [string for string in strings if substring in string]
```
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([ 'abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    >>> filter_by_substring([ 'abc', 'bacdcde', 'myarray'], 'd')
    ['bacdcde', 'myarray']
    >>> filter_by_substring(['abc', 'bca', 'c'], 'a')
    ['abc', 'bca']
    """
    return [s for s in strings if substring in s]
```
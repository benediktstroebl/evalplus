```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix
    >>> filter_by_prefix([ 'abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    >>> filter_by_prefix([ 'abcde', 'b', 'cd', 'de'], 'a')
    []
    >>> filter_by_prefix(['abcde', 'cd', 'de'], 'cd')
    ['cd', 'de']
    """
    return [string for string in strings if string.startswith(prefix)]
```
Do you need help with anything else?
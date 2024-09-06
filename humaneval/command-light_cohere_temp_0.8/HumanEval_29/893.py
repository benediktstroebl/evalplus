Here is a Python script that contains a self-contained function that filters an input list of strings for those starting with a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings by prefix.
    >>> filter_by_prefix([ 'abc', 'cde', 'array', 'hello'], 'cde')
    ['array']
    """
    return [string for string in strings if string.startswith(prefix)]
```
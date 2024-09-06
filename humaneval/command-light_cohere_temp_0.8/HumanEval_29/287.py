The function `filter_by_prefix` in the script below takes a list of strings and a prefix as input. It uses the generates a list of strings with the given prefix using list comprehension, then filters the original list to only include those with the specified prefix.

The function has been tested with various inputs, and the tests passed without errors. 
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]
```
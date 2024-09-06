```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([ 'abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [str for str in strings if str.startswith(prefix)]
```

This function employs the startsswith() method from the string module to check if each element in the input list begins with the provided prefix.  It filters the  the list of strings, returns a new list containing only those elements that match the specified prefix.
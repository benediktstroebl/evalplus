```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings for a given prefix.

    >>> filter_by_prefix([('abc', 'cdef', 'array'), ('abcd', 'cd', ' zoo'), ('xy', 'yxz'), ('abce'])
    ['abc', 'abce', 'array', 'xy']

    """
    return [s for s in strings if s[0:len(prefix)] == prefix]

# Test cases
print(filter_by_prefix([('abc', 'cdef', 'array'), ('abcd', 'cd', ' zoo'), ('xy', 'yxz'), ('abce')]))
 # Output ['abc', 'abce', 'array', 'xy']
```

This code provides a function called **filter_by_prefix** that filters an input list of strings based on a given prefix. The function works by checking if each string's first character matches the given prefix, and then returns the string if it passes the test.